from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import WoodruffWorld

from .woodruff_data import ITEM_BY_NAME, Flag


class WoodruffItem(Item):
    game = "Woodruff and the Schnibble of Azimuth"


# Make item list
class WoodruffItemDataType(IntEnum):
    INVENTORY_ITEM = 1000
    FLAG_ITEM = 2000

@dataclass(frozen=True)
class WoodruffItemData:
    id: int
    name: str
    type: WoodruffItemDataType
    classification: ItemClassification
    data_id: int
    data_value: int | None = None

AP_ITEMS = set()

# Add inventory items
normal_inventory_items = [
    "Button", "Azimuth photo", "Bluxtre pulp", "Brush", "Feathers", "Coffee", "Weather watch", "Rummy rules", "Bean",
    "Can", "Kite", "Morphoplastoc eye", "\"A\" stone", "Azimuth article", "Tobozon", "Breath certificate",
    "Prison form", "Morphoplastoc finger", "Shirt"
]
for item_name in normal_inventory_items:
    data_item = ITEM_BY_NAME[item_name]
    AP_ITEMS.add(WoodruffItemData(
        id=WoodruffItemDataType.INVENTORY_ITEM + data_item.id,
        name=item_name,
        type=WoodruffItemDataType.INVENTORY_ITEM,
        classification=ItemClassification.progression,
        data_id=data_item.id
    ))

# Add flag items
AP_ITEMS.add(WoodruffItemData(
    id=WoodruffItemDataType.FLAG_ITEM + Flag.SKILL_READ,
    name="Reading skill",
    type=WoodruffItemDataType.FLAG_ITEM,
    classification=ItemClassification.progression,
    data_id=Flag.SKILL_READ,
    data_value=1
))


AP_ITEM_NAME_TO_ID: dict[str, int] = {i.name: i.id for i in AP_ITEMS}
AP_ITEM_BY_NAME: dict[str, WoodruffItemData] = {i.name: i for i in AP_ITEMS}
AP_ITEM_BY_ID: dict[int, WoodruffItemData] = {i.id: i for i in AP_ITEMS}


def create_item_with_correct_classification(world: WoodruffWorld, name: str) -> WoodruffItem:
    ap_item = AP_ITEM_BY_NAME[name]
    return WoodruffItem(ap_item.name, ap_item.classification, ap_item.id, world.player)


def create_all_items(world: WoodruffWorld) -> None:
    item_list = AP_ITEMS

    itempool: list[WoodruffItem] = [world.create_item(i.name) for i in item_list]
    world.multiworld.itempool += itempool

    world.shuffled_items = {i.id for i in item_list if i.type == WoodruffItemDataType.INVENTORY_ITEM}

