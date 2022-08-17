import bpy

for obj in bpy.context.selected_objects:
    bpy.context.view_layer.objects.active = obj

    if obj.parent is not None:
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

    oblocation = (obj.location[0], obj.location[1], obj.location[2])
    obRotation = (obj.rotation_euler[0], obj.rotation_euler[1], obj.rotation_euler[2])

    print(oblocation, obRotation)

    obj.location = [0, 0, 0]
    obj.rotation_euler = [0, 0, 0]

    emptyName = "SM_" + obj.name

    empty = bpy.data.objects.new("empty", None)
    bpy.context.scene.objects.link(empty)
    empty.empty_draw_size = 15
    empty.empty_draw_type = 'CUBE'
    empty.name = emptyName
    empty.select_set(True)

    obj.parent = empty
    empty.location = oblocation
    empty.rotation_euler = obRotation
