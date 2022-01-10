#!/usr/bin/env python3
import bpy
import sys
from pathlib import Path

def addObjectToLoacation(x, y, z,h):
    bpy.ops.mesh.primitive_cube_add(location=(x,y,z), scale=(0.15,0.15,h))
    bpy.ops.transform.translate(value=(0, 0, h))
    return

if __name__ == "__main__":
    
    #clean the scene of default cube and camera
    while bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[0], do_unlink=True)

    data = [] 

    #get arguments
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]

    path = argv[0] #coordinates txt file path
    arena = argv[1]
    output="export.stl"
    output2="export.dae"

    #read file
    with open(path) as file:
        content = file.readlines()
        for line in content:
            data.append(line.strip())
            
    #get context and import arena   
    context = bpy.context
    importedArena = bpy.ops.import_scene.obj(filepath=arena)
    

    #parse obstacle data and place obstacles in arena
    for line in data:
        try:
            splitedLine=line.split(",")
            addObjectToLoacation(float(splitedLine[0]), float(splitedLine[1]), float(splitedLine[2]), 1)
            
        except Exception as error:
            print (error)
            

    #export combined STL file
    bpy.ops.export_mesh.stl(filepath=output, axis_forward="Y", axis_up="Z")
    bpy.ops.wm.collada_export(filepath=output2, export_global_forward_selection="Y", export_global_up_selection="Z")
    print(":: both exports finshed ::")