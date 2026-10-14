import struct
from typing import Optional

import pymem


class WoodruffMemory:
    SCUMMVM_PROCESS = "scummvm.exe"
    INVENTORY_SIGNATURES = [
        b"BUTTON\x00{26}.{8}BOOT\x00", # EN
        b"BOUTON\x00{26}.{8}BOTTE\x00", # FR
    ]

    INVENTORY_OFFSET = 0x4F70 # 20336
    INVENTORY_ITEM_LENGTH = 0x28 # 40 bytes

    GAME_FLAG_OFFSET = 0x6C80 # 27776

    ENTITY_HOTSPOT_OFFSET = 0x28F0 # 10480
    ENTITY_HOTSPOT_LENGTH = 0x10  # 16 bytes
    CHAR_HOTSPOT_OFFSET = 0x3048 # 12360
    CHAR_HOTSPOT_LENGTH = 0x0C # 12 bytes
    INTERACTED_HOTSPOT_OFFSET = 0x00F0  # 240

    MULT_OBJECT_OFFSET = 0x1150 # 4432
    MULT_OBJECT_LENGTH = 0x28 # 40 bytes

    CURRENT_ZONE_OFFSET = 0x0DC2 # 3522


    def __init__(self):
        self._process: Optional[pymem.Pymem] = None
        self._vars_address: Optional[int] = None


    ##################
    # Process
    ##################

    def attach_process(self) -> bool:
        try:
            self._process = pymem.Pymem(self.SCUMMVM_PROCESS)
            return True
        except pymem.exception.ProcessNotFound:
            return False

    def is_process_attached(self) -> bool:
        return self._process is not None

    def detect_base_address(self) -> bool:
        if not self.is_process_attached():
            raise RuntimeError("Trying to detect base memory address but process is not attached")

        for signature in self.INVENTORY_SIGNATURES:
            inventory_address = pymem.pattern.pattern_scan_all(
                self._process.process_handle,
                signature,
                return_multiple=False
            )
            if inventory_address:
                self._vars_address = inventory_address - self.INVENTORY_OFFSET
                return True

        return False


    ##################
    # Inventory
    ##################

    def get_inventory_flag(self, item_index: int, offset: int) -> int:
        return self.read_var8(self.INVENTORY_OFFSET + item_index * self.INVENTORY_ITEM_LENGTH + offset)

    def set_inventory_flag(self, item_index: int, offset: int, value: int) -> None:
        return self.write_var8(self.INVENTORY_OFFSET + item_index * self.INVENTORY_ITEM_LENGTH + offset, value)


    ##################
    # Game flags
    ##################

    def get_game_flag(self, flag: int) -> int:
        return self.read_var16_signed(self.GAME_FLAG_OFFSET + flag * 2)

    def set_game_flag(self, flag: int, value: int) -> None:
        return self.write_var16(self.GAME_FLAG_OFFSET + flag * 2, value)


    ##################
    # Hotspots
    ##################

    def get_interacted_hotspot_id(self) -> int:
        return self.read_var32(self.INTERACTED_HOTSPOT_OFFSET)

    def get_hotspot_address(self, hotspot_id: int) -> int:
        if 0 <= hotspot_id <= 64:
            return self.ENTITY_HOTSPOT_OFFSET + hotspot_id * self.ENTITY_HOTSPOT_LENGTH
        elif 200 <= hotspot_id <= 219:
            return self.CHAR_HOTSPOT_OFFSET + hotspot_id * self.CHAR_HOTSPOT_LENGTH
        else:
            raise RuntimeError("Invalid hotspot index")

    def get_hotspot_position(self, hotspot_id: int) -> tuple[int, int]:
        address = self.get_hotspot_address(hotspot_id)
        return self.read_var16(address), self.read_var16(address + 2)

    def set_hotspot_position(self, hotspot_id: int, position: tuple[int, int]) -> None:
        address = self.get_hotspot_address(hotspot_id)
        self.write_var16(address, position[0])
        self.write_var16(address + 2, position[1])


    ##################
    # Mult objects
    ##################

    def get_mult_object_flag(self, object_id: int, offset: int) -> int:
        return self.read_var8(self.MULT_OBJECT_OFFSET + object_id * self.MULT_OBJECT_LENGTH + offset)

    def set_mult_object_flag(self, object_id: int, offset: int, value: int) -> None:
        return self.write_var8(self.MULT_OBJECT_OFFSET + object_id * self.MULT_OBJECT_LENGTH + offset, value)


    ##################
    # Current zone
    ##################

    def get_current_zone_id(self) -> int:
        return self.read_var16(self.CURRENT_ZONE_OFFSET)



    ##################
    # Low level reading
    ##################

    def read_var(self, offset: int, length: int) -> bytes:
        if not self.is_process_attached():
            raise RuntimeError("Process is not attached")
        return self._process.read_bytes(self._vars_address + offset, length)

    def read_var8(self, offset: int) -> int:
        data = self.read_var(offset, 1)
        return struct.unpack_from("<B", data)[0]

    def read_var8_signed(self, offset: int) -> int:
        data = self.read_var(offset, 1)
        return struct.unpack_from("<b", data)[0]

    def read_var16(self, offset: int) -> int:
        data = self.read_var(offset, 2)
        return struct.unpack_from("<H", data)[0]

    def read_var16_signed(self, offset: int) -> int:
        data = self.read_var(offset, 2)
        return struct.unpack_from("<h", data)[0]

    def read_var32(self, offset: int) -> int:
        data = self.read_var(offset, 4)
        return struct.unpack_from("<I", data)[0]

    def read_var32_signed(self, offset: int) -> int:
        data = self.read_var(offset, 4)
        return struct.unpack_from("<i", data)[0]

    def read_var_string(self, offset: int, max_length: int = 128) -> str:
        data = self.read_var(offset, max_length)
        null_pos = data.find(b"\x00")
        raw = data[:null_pos] if null_pos != -1 else data
        return raw.decode("latin-1")


    ##################
    # Low level writing
    ##################

    def write_var(self, offset: int, data: bytes, length:int) -> None:
        if not self.is_process_attached():
            raise RuntimeError("Process is not attached")
        self._process.write_bytes(self._vars_address + offset, data, length)

    def write_var8(self, offset: int, value: int) -> None:
        self.write_var(offset, struct.pack("<B", value & 0xFF), 1)

    def write_var16(self, offset: int, value: int) -> None:
        self.write_var(offset, struct.pack("<H", value & 0xFFFF), 2)

    def write_var32(self, offset: int, value: int) -> None:
        self.write_var(offset, struct.pack("<I", value & 0xFFFFFFFF), 4)

    def write_var_string(self, offset: int, value: str, max_length: int = 128) -> None:
        encoded = value.encode("latin-1")[:max_length - 1] + b"\x00"
        self.write_var(offset, encoded, len(encoded))

