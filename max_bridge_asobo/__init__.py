"""
Blender bridge, easily send assets to 3ds Max.

### WARNING: Addon is part of the MSFS 2024 SDK and is available to the public. ### 
"""
# Reload
if "bpy" in locals():
    import sys
    import importlib

    current_package_prefix = f"{__name__}."
    for name, module in sys.modules.copy().items():
        if name.startswith(current_package_prefix):
            print(f"Reloading {name}")
            importlib.reload(module)

bl_info = {
    "name": "Asobo: 3ds Max Bridge",
    "author": "Asobo Studio (Mathieu Richecoeur)",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    "description": "Transfer 3D Models between 3ds Max and Blender.",
    "location": "View3D > Tool Shelf > 3ds Max Bridge",
    "warning": "",
    "doc_url": "",
    "category": "Tools",
}

# region ######################### REGISTRATION #################################


def register():
    from max_bridge_asobo.ui import bridge_panel
    from max_bridge_asobo import addon_prefs, server
    bridge_panel.register()
    addon_prefs.register()
    server.register()

def unregister():
    from max_bridge_asobo.ui import bridge_panel
    from max_bridge_asobo import addon_prefs, server
    bridge_panel.unregister()
    addon_prefs.unregister()
    server.unregister()
# endregion
