import bpy

for ob in bpy.context.selected_objects:
    bpy.context.view_layer.objects.active = ob
    bpy.ops.object.game_property_new(name="Test", type="BOOL")
    
#type: 'BOOL', 'INT', 'FLOAT', 'STRING', 'TIMER'
