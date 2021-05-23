#Simple Texture Extension Switcher (Maya)

import maya.cmds as cmds

gExt = raw_input()

#Get Selection
getSel = cmds.ls(sl = True, dag = True)

#Loop through selected objects
for obj in getSel:
    #Get Shading Group & Connected Materials
    gSGrp = cmds.listConnections(getSel[obj], type='shadingEngine') 
    gMtl  = cmds.ls(cmds.listConnections(gSGrp), mat = True)

    #Loop Material Textures & Switch File Extensions
    for i in gMtl:
        gTex = cmds.listConnections(i, type='file')

        for j in gTex:
            toSwitch = cmds.getAttr('%s.fileTextureName' % j)
            cmds.setAttr(('%s.fileTextureName' % j),(toSwitch.rsplit('.', 1)[0]+'.'+str(gExt)),type='string')
