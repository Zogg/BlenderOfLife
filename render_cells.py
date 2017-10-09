import json
import bpy

edgelen = 1

config = None
with open("config.json", "r") as f:
    config = json.load(f)

bpy.ops.mesh.primitive_cube_add()
init_cube = bpy.data.objects["Cube"]

with open(config['data_file'], "r") as f:
    generations = json.load(f)

    for z, cells in enumerate(generations):
        for coords in cells:
            new_cube = init_cube.copy()
            new_cube.location.z = z
            new_cube.location.x = coords[0]
            new_cube.location.y = coords[1]
            bpy.context.scene.objects.link(new_cube)
            #bpy.ops.mesh.primitive_cube_add(location=(coords[0], coords[1], z), radius=edgelen / 2)


    bpy.ops.wm.save_mainfile(filepath=config['blender_output_file'])
