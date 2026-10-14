from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, CanReachRegion, HasAll

if TYPE_CHECKING:
    from .world import WoodruffWorld


def set_all_rules(world: WoodruffWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)


def set_all_entrance_rules(world: WoodruffWorld) -> None:
    # Access to Administration center
    adm_entrance = world.get_entrance("Azimuth's house to Administration Center")
    world.set_rule(adm_entrance, Has("Reading skill"))

    # Access to Clandestine Gaming Room
    cgr_entrance = world.get_entrance("Cui-cui store to Clandestine Gaming Room")
    world.set_rule(cgr_entrance, Has("Morphoplastoc finger"))

    # Access to Bigwig's Area
    bga_entrance = world.get_entrance("Brotoflatron's Plazza to Bigwig's Area")
    world.set_rule(bga_entrance, CanReachRegion("Virtual Trip Tower"))

    # Access to prison
    prc_entrance = world.get_entrance("Slammer's Dead End to Prison's Courtyard")
    world.set_rule(prc_entrance, Has("Prison form"))

    # Access to factory
    fac_entrance = world.get_entrance("Factory's Front yard to Hat Division")
    world.set_rule(fac_entrance, Has("Breath certificate")) # TODO

    # Access to boozook temple
    tp1_entrance = world.get_entrance("Temple's Front yard to Temple's Hallways level 1")
    world.set_rule(tp1_entrance, Has("Bluxtre pulp"))


def set_all_location_rules(world: WoodruffWorld) -> None:

    has_meteo = HasAll("Tobozon", "Weather watch")
    can_acess_meteorite_region = (
        CanReachRegion("Administration Center") |
        CanReachRegion("Brotoflatron's Plazza") |
        CanReachRegion("Bigwig's Area")
    )

    world.set_rule(world.get_location("Item: Bluxtre pulp"), CanReachRegion("Temple's Front yard") & has_meteo & can_acess_meteorite_region)
    world.set_rule(world.get_location("Item: Weather watch"), Has("Coffee"))
    world.set_rule(world.get_location("Item: Rummy rules"), Has("Coffee") & CanReachRegion("Experimentation Lab"))
    world.set_rule(world.get_location("Item: Kite"), CanReachRegion("Experimentation Lab"))
    world.set_rule(world.get_location("Item: Morphoplastoc eye"), CanReachRegion("Virtual Trip Tower") & CanReachRegion("Experimentation Lab"))
    world.set_rule(world.get_location("Item: Azimuth article"), Has("Azimuth photo"))
    world.set_rule(world.get_location("Item: Tobozon"), Has("\"A\" stone"))
    world.set_rule(world.get_location("Item: Breath certificate"), CanReachRegion("Experimentation Lab"))
    world.set_rule(world.get_location("Item: Prison form"), CanReachRegion("Experimentation Lab"))

