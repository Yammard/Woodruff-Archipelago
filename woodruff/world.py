from typing import Mapping, Any

from worlds.AutoWorld import World
from . import locations, items, regions, rules


class WoodruffWorld(World):
    game = "Woodruff and the Schnibble of Azimuth"

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.AP_ITEM_NAME_TO_ID
    origin_region_name = "Azimuth's house"

    shuffled_items: list[int] = []

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.WoodruffItem:
        return items.create_item_with_correct_classification(self, name)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "shuffled_items": self.shuffled_items,
        }



