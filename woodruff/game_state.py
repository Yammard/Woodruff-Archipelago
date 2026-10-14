from CommonClient import logger
from .memory import WoodruffMemory
from .woodruff_data import Zone, ZONE_BY_ID, LOCATIONS, Location, InteractionCheck, FlagCheck, HotspotPositionCheck, \
    Check


class WoodruffGameState:
    _memory: WoodruffMemory

    current_zone: Zone | None
    completed_locations: set[int]

    def __init__(self, memory: WoodruffMemory):
        self._memory = memory

        self.current_zone = None

        self.completed_locations = set()


    def update(self) -> None:
        zone_id = self._memory.get_current_zone_id()
        if not ZONE_BY_ID[zone_id]:
            raise RuntimeError("Unknown zone")

        zone = ZONE_BY_ID[zone_id]
        if zone != self.current_zone:
            logger.info("Entered new zone : " + zone.name)
            self.current_zone = zone

        self.process_new_locations()

    def add_inventory_item(self, item_id: int) -> None:
        self._memory.set_inventory_flag(item_id, 39, 1)

    def deactivate_inventory_item(self, item_id: int) -> None:
        self._memory.set_inventory_flag(item_id, 37, 50)

    def activate_inventory_item(self, item_id: int) -> None:
        self._memory.set_inventory_flag(item_id, 37, 250)

    def mark_inventory_item_as_received(self, item_id: int) -> None:
        self._memory.set_inventory_flag(item_id, 34, 1)

    def has_received_inventory_item(self, item_id: int) -> bool:
        return self._memory.get_inventory_flag(item_id, 34) == 1

    def set_game_flag(self, flag: int, value: int) -> None:
        self._memory.set_game_flag(flag, value)

    def get_game_flag(self, flag: int) -> int:
        return self._memory.get_game_flag(flag)


    def process_new_locations(self):
        if self.current_zone is None:
            return

        for location in LOCATIONS:
            if location.zone_key == self.current_zone.key or location.zone_key is None:
                if location.id not in self.completed_locations and self.location_completed(location):
                    self.completed_locations.add(location.id)

    def location_completed(self, location: Location) -> bool:
        if self.current_zone is not None and self.current_zone.key != location.zone_key:
            return False

        return any(
            all(self.check_is_valid(check) for check in group)
            for group in location.checks
        )

    def check_is_valid(self, check: Check) -> bool:
        if isinstance(check, FlagCheck):
            return check.min <= self._memory.get_game_flag(check.flag) <= check.max

        if isinstance(check, InteractionCheck):
            return (
                    check.entity.zone == self.current_zone
                    and check.entity.hotspot_id == self._memory.get_interacted_hotspot_id()
            )

        if isinstance(check, HotspotPositionCheck):
            if check.entity.zone != self.current_zone:
                return False
            position = self._memory.get_hotspot_position(check.entity.hotspot_id)
            return tuple(position) == (check.x, check.y)

        raise TypeError(f"Check inconnu : {check!r}")


