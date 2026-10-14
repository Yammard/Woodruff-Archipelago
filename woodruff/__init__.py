from .world import WoodruffWorld as WoodruffWorld

# Client registration
from worlds.LauncherComponents import Component, components, Type, launch as launch_component, icon_paths
def launch_client(*args):
    from .client import launch
    launch_component(launch, name="Woodruff Client", args=args)

components.append(Component("Woodruff Client",
                           game_name="Woodruff and the Schnibble of Azimuth",
                           func=launch_client,
                           component_type=Type.CLIENT,
                           supports_uri=True))