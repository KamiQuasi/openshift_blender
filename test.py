import json
import bpy

verts = [(0,0,0),(0,2,0),(2,2,0),(2,0,0)]
faces = [(0,1,2,3)]

scn = bpy.context.scene

# Camera
cam = bpy.data.cameras.new("Camera1")
cam1.lens = 35



mesh = bpy.data.meshes.new("Plane")
object = bpy.data.objects.new("Plane", mesh)

bpy.context.collection.objects.link(object)

mesh.from_pydata(verts,[],faces)


#bpy.context.area.ui_type = 'GeometryNodeTree'
#bpy.ops.node.new_geometry_nodes_modifier()
#bpy.ops.node.add_node(type="GeometryNodePointInstance", use_transform=True)
#bpy.ops.node.translate_attach_remove_on_cancel(TRANSFORM_OT_translate={"value":(-47.8838, -12.6768, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":True, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False}, NODE_OT_attach={}, NODE_OT_insert_offset={})

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.space_data.context = 'OUTPUT' # the output settings
bpy.context.scene.render.resolution_x = 600
bpy.context.scene.render.resolution_y = 480

bpy.context.scene.frame_start = 5
bpy.context.scene.frame_end = 60
bpy.context.scene.frame_step = 5

bpy.context.scene.render.filepath = "/tmp/foo.png"


bpy.context.scene.cycles.use_denoising = True
bpy.context.scene.cycles.denoiser = 'OPENIMAGEDENOISE'

bpy.context.scene.cycles.max_bounces = 4

bpy.context.scene.view_settings.view_transform = 'Standard'


bpy.context.scene.render.use_border = True
bpy.ops.view3d.render_border(xmin=286, xmax=441, ymin=298, ymax=446)
#bpy.ops.view3d.clear_render_border()
bpy.context.scene.render.use_crop_to_border = False


data = '[{"asset":"Cash","value":12},{"asset":"Inventory","value":15},{"asset":"Equipment","value":50}]'
data_dict = json.loads(data)

print(data_dict)


#print(data_dict.value)
