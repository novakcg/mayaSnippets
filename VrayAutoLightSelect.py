#Automatically Create Light Selects (Diffuse, Spec)

import maya.cmds as cmds
import maya.mel as mel

#Get Selection 
lgtSel = cmds.ls(sl = True)

#Loop Through Selection Creating LightSelectElements, Naming, and Linking Sets.
for lgt in lgtSel:
    print lgt
    mel.eval("vrayAddRenderElement LightSelectElement;")
    mel.eval("""rename vrayRE_Light_Select "LS_""" + lgt + """_SPEC";""")
    
    mel.eval("vrayAddRenderElement LightSelectElement;")
    mel.eval("""rename vrayRE_Light_Select "LS_""" + lgt + """_DIFF";""")
    
    mel.eval("""vraySetAttr("LS_""" + lgt + """_SPEC", "vray_type_lightselect", "3", "int");""")
    mel.eval("""setAttr -type "string" LS_""" + lgt + """_SPEC.vray_name_lightselect "LS_""" + lgt + """_SPEC";""")
    mel.eval("""sets -add LS_""" + lgt + """_SPEC """ + lgt)
     
    mel.eval("""vraySetAttr("LS_""" + lgt + """_DIFF", "vray_type_lightselect", "2", "int");""")
    mel.eval("""setAttr -type "string" LS_""" + lgt + """_DIFF.vray_name_lightselect "LS_""" + lgt + """_DIFF";""")
    mel.eval("""sets -add LS_""" + lgt + """_DIFF """ + lgt)
