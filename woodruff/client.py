import asyncio
from typing import Any

from CommonClient import CommonContext, server_loop, logger
from .game_state import WoodruffGameState
from .items import AP_ITEM_BY_ID, WoodruffItemDataType
from .memory import WoodruffMemory


class WoodruffContext(CommonContext):
    game = "Woodruff and the Schnibble of Azimuth"
    items_handling = 0b111

    client_loop: asyncio.Task[None]
    game_state: WoodruffGameState | None

    processed_item_index: int = 0
    slot_data: dict[str, Any]


    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            for item_id in self.slot_data["shuffled_items"]:
                data_id = AP_ITEM_BY_ID[item_id].data_id
                if not self.game_state.has_received_inventory_item(data_id):
                    self.game_state.deactivate_inventory_item(data_id)


    async def client_loop(self) -> None:
        memory = WoodruffMemory()
        logger.info("Attaching to " + memory.SCUMMVM_PROCESS + " ...")
        if not memory.attach_process():
            logger.error("Failed to attach process. Is ScummVM running ?")
            return

        logger.info("Attached to " + memory.SCUMMVM_PROCESS)
        logger.info("Waiting for the game to be in a valid state ...")

        while not memory.detect_base_address():
            await asyncio.sleep(1)

        self.game_state = WoodruffGameState(memory)
        logger.info("Ready !")

        while not self.exit_event.is_set():
            self.game_state.update()
            await self.handle_new_locations()
            self.handle_received_items()


            await asyncio.sleep(0.1)


    async def handle_new_locations(self) -> None:
        new_locations = self.game_state.completed_locations - self.locations_checked
        for location in new_locations:
            self.locations_checked.add(location)
            await self.check_locations({location})

    def handle_received_items(self) -> None:
        new_items = self.items_received[self.processed_item_index:]
        for item in new_items:
            logger.info("Received new item: " + str(item))
            ap_item = AP_ITEM_BY_ID[item.item]
            match ap_item.type:
                case WoodruffItemDataType.INVENTORY_ITEM:
                    self.game_state.activate_inventory_item(ap_item.data_id)
                    self.game_state.add_inventory_item(ap_item.data_id)
                case WoodruffItemDataType.FLAG_ITEM:
                    self.game_state.set_game_flag(ap_item.data_id, ap_item.data_value)
            self.processed_item_index += 1




async def main() -> None:
    ctx = WoodruffContext(None, None)

    ctx.run_gui()
    ctx.server_task = asyncio.create_task(server_loop(ctx))
    ctx.client_task = asyncio.create_task(ctx.client_loop())

    await ctx.exit_event.wait()
    await ctx.shutdown()

def launch(*launch_args) -> None:
    asyncio.run(main())

