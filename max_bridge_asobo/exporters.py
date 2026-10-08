import bpy

# do not import using from in order to prevent circular import
import max_bridge_asobo.addon_prefs as addon_prefs 

from max_bridge_asobo.bridge_base import obj_utils
from max_bridge_asobo.bridge_base.usd_export import GenericUSDExporter

exporter_classes = [GenericUSDExporter]

def register_exporter_class(exporter: type[GenericUSDExporter]):
    if exporter not in exporter_classes:
        exporter_classes.append(exporter)

def unregister_exporter_class(exporter: type[GenericUSDExporter]):
    if exporter in exporter_classes:
        exporter_classes.remove(exporter)

def get_exporter_classes()->list[type[GenericUSDExporter]]:
    global exporter_classes
    return  exporter_classes
                           
def get_current_exporter(addon_prefs: addon_prefs.BridgePreferences) -> None | type[GenericUSDExporter]:

    for exp in get_exporter_classes():
        if exp.ID == addon_prefs.bridge_preset:
            return exp
    return None

def send_selected():
    current_exporter = get_current_exporter(addon_prefs.get_addon_prefs())
    if current_exporter:
        current_exporter.send_selected_to_max_socket()

def send_all(scene: bpy.types.Scene, view_layer: bpy.types.ViewLayer):
    obj_utils.select_all_scene(scene, view_layer)
    send_selected()


# region Scene Properties
def get_presets_for_enum_prop() -> list[tuple[str]]:
    exporter_presets = []
    for exp in get_exporter_classes():
        exporter_presets.append((exp.ID, exp.PRESET_UI_LABEL, ""))
    return exporter_presets

# endregion
def register():
    global exporter_classes
    exporter_classes = [GenericUSDExporter]

def unregister():
    global exporter_classes
    exporter_classes = []