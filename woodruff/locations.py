from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import WoodruffWorld

from .woodruff_data import LOCATIONS, ZONE_BY_KEY


class WoodruffLocation(Location):
    game = "Woodruff and the Schnibble of Azimuth"


LOCATION_NAME_TO_ID: dict[str, int] = {l.name: l.id for l in LOCATIONS}

def create_all_locations(world: WoodruffWorld) -> None:
    for loc in LOCATIONS:
        if loc.zone_key in ["STS", "BRS"]:
            match loc.name:
                case "Item: Boot" | "Item: Nut":
                    region = world.get_region("Bridge of the Slums (Left)")
                case "Item: Can" | "Item: Bean" | "Item: Morphoplastoc eye":
                    region = world.get_region("Stairs Street (Left)")
                case "Item: Kite":
                    region = world.get_region("Stairs Street (Right)")
                case _:
                    region = world.get_region(ZONE_BY_KEY[loc.zone_key].name)

        elif loc.zone_key is not None:
            region = world.get_region(ZONE_BY_KEY[loc.zone_key].name)

        else:
            region = world.get_region("Azimuth's house")

        region.add_locations({loc.name: loc.id})

