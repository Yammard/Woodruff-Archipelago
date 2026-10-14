from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import WoodruffWorld

from .woodruff_data import ZONES, ZONE_BY_KEY


def create_and_connect_regions(world: WoodruffWorld) -> None:
    # Create regions
    for zone in ZONES:

        if zone.key in ["STS", "BRS"]:
            # Zone must be split
            for sub in ["Left", "Right"]:
                world.multiworld.regions.append(
                    Region(zone.name + " (" + sub + ")", world.player, world.multiworld)
                )
        else:
            # Normal case
            world.multiworld.regions.append(
                Region(zone.name, world.player, world.multiworld)
            )

    # Connect regions
    for zone in ZONES:

        if zone.key == "STS":

            left = world.get_region("Stairs Street (Left)")
            right = world.get_region("Stairs Street (Right)")
            left.connect(right)
            left.connect(world.get_region("Wino's Alley"))
            right.connect(left)
            right.connect(world.get_region("Azimuth's house"))

        elif zone.key == "BRS":

            left = world.get_region("Bridge of the Slums (Left)")
            right = world.get_region("Bridge of the Slums (Right)")
            left.connect(right, "Bridge of the Slums (Left) to Bridge of the Slums (Right)")
            left.connect(world.get_region("Street of the Sad Boozook"), "Bridge of the Slums (Left) to Street of the Sad Boozook")
            right.connect(left, "Bridge of the Slums (Right) to Bridge of the Slums (Left)")
            right.connect(world.get_region("Wino's Alley"), "Bridge of the Slums (Right) to Wino's Alley")

        else:

            region = world.get_region(zone.name)
            for adj in zone.connections:
                if zone.key == "AZI" and adj == "STS":
                    adj_region = world.get_region("Stairs Street (Right)")
                elif zone.key == "WNO" and adj == "STS":
                    adj_region = world.get_region("Stairs Street (Left)")
                elif zone.key == "MEM" and adj == "STS":
                    adj_region = world.get_region("Stairs Street (Left)")
                elif zone.key == "SAD" and adj == "BRS":
                    adj_region = world.get_region("Bridge of the Slums (Left)")
                elif zone.key == "WNO" and adj == "BRS":
                    adj_region = world.get_region("Bridge of the Slums (Right)")
                else:
                    adj_region = world.get_region(ZONE_BY_KEY[adj].name)

                region.connect(adj_region, region.name + " to " + adj_region.name)

