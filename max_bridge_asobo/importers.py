import json

from max_bridge_asobo import addon_prefs

from max_bridge_asobo.bridge_base import path_utils, ui_utils
from max_bridge_asobo.bridge_base.usd_import import GenericUSDImporter

importer_classes = [GenericUSDImporter]

def register_importer_class(importer: type[GenericUSDImporter]):
    if importer not in importer_classes:
        importer_classes.append(importer)

def unregister_importer_class(importer: type[GenericUSDImporter]):
    if importer not in importer_classes:
        importer_classes.remove(importer)


def get_importer_classes()->list[type[GenericUSDImporter]]:
    global importer_classes
    return  importer_classes

def get_current_importer(addon_prefs: addon_prefs.BridgePreferences) -> None | type[GenericUSDImporter]:

    for imp in get_importer_classes():
        if imp.ID == addon_prefs.bridge_preset:
            return imp
    return None


def import_bridge_usd(usd_path:str):
    """Import bridge usd using correct importer.

    Args:
        usd_path: absolute usd path.
    """
    json_data : dict= {}
    json_path = path_utils.get_associated_json(usd_path)
    with open(json_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    exporter_name = json_data.get("exporter",None)
    from_dcc_name = json_data.get("from_dcc",None)

    importer_class = None
    for imp in get_importer_classes():
        if imp.ID == exporter_name and imp.TARGET_DCC == from_dcc_name:
            importer_class = imp
    
    if not importer_class:
        ui_utils.message_popup(
                ui_utils.PopUpLevel.CRITICAL,
                title="Import Error",
                message="No importer found for this USD.",
            )
        return
    importer_class.import_usd(usd_path)

def register():
    global importer_classes
    importer_classes = [GenericUSDImporter]

def unregister():
    global importer_classes
    importer_classes = []