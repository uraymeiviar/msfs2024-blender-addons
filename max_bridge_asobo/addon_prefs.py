import bpy


def _get_preset_items(_self, context: bpy.types.Context)->list[tuple[str, str, str]]:
    import max_bridge_asobo.exporters as exporters #do not import using from in order to prevent circular import
    return exporters.get_presets_for_enum_prop()

class BridgePreferences(bpy.types.AddonPreferences):
    bl_idname = __package__


    bridge_preset : bpy.props.EnumProperty(
            name="Bridge Preset",
            description="Affects how assets are exported",
            items=_get_preset_items,
            default=0
        ) # type: ignore
    
    reuse_existing_collections: bpy.props.BoolProperty(
        name="Reuse Existing Collections",
        description=("Reuse existing collections with the same names when\n" 
                     "recreating 3ds Max layers in Blender.\n"
                    "Consider enabling this option when importing\n"
                    "multiple times into the same scene to prevent\n"
                    "duplicated collections."),
        default=False,
    )  # type: ignore


def get_addon_prefs() -> BridgePreferences:
    return bpy.context.preferences.addons[__package__].preferences

classes = ( 
    BridgePreferences,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
