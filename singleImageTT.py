import maya.cmds as cmds
import pymel.core as pm
import webbrowser

PROJECT_DIR = "/PathToProject"

#Get selection (pos) where the lights will be placed.
cmds.select('lgtSpin24')
getSel = cmds.ls(sl = True)

#Return XYZ Position as a 1D Array
def getLocXYZ(mesh):
    x = cmds.getAttr(str(getSel[0])+".translateX")
    y = cmds.getAttr(str(getSel[0])+".translateY")
    z = cmds.getAttr(str(getSel[0])+".translateZ")
    return[x,y,z]

lgtPos = getLocXYZ(getSel[0])

#Import Maya File (LightRig)
cmds.file('TTlightRig.mb', i = True)
cmds.select('grpLights')

#Move Lights To Location Specified (pos)
cmds.move(lgtPos[0], lgtPos[1], lgtPos[2])
cmds.select('grpLights')

#Select Invidual Lights in Group & Store To List
cmds.select(cmds.listRelatives(cmds.ls(sl=True), children=True))
lightSel = cmds.ls(sl = True)
lightsTT = lightSel

# Create a empty counter
j = 0

#Going through all lights, creating light sets and adding/linking them to the lights
for light in lightSel:
    mel.eval("vrayAddRenderElement LightSelectElement;")
    mel.eval("""rename vrayRE_Light_Select "LS_""" + light + """_DIFF";""")
    mel.eval("""vraySetAttr("LS_""" + light + """_DIFF", "vray_type_lightselect", "2", "int");""")
    mel.eval("""setAttr -type "string" LS_""" + light + """_DIFF.vray_name_lightselect \" """ + str(j) + """\";""")
    mel.eval("""sets -add LS_""" + light + """_DIFF """ + light)
    
    #Increment Counter
    j+=1;
    
#Define Render Settings / Set Project & Render
pm.ls('vraySettings')[0]
cmds.setAttr("vraySettings.imageFormatStr", 'jpg', type='string')
cmds.setAttr("vraySettings.fileNamePrefix", "frame", type='string')
cmds.setAttr("vraySettings.animType", 0)
pm.mel.setProject(PROJECT_DIR)
pm.vrend()

#Clean-up 
for light in lightsTT:
    cmds.select(light)
    cmds.delete()
    
cmds.select("grpLights")
cmds.delete()

cmds.select("lgtSpin24")
cmds.delete()

#Display Webpage
webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(PROJECT_DIR + "interactiveTT.html")
