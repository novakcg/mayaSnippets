#Animation of Unhiding Object By Object In Selection Order

import maya.cmds as cmds

#Get Selection
getSel = cmds.ls(sl = True)

#Loop through all objects setting Visibility to Off.
for i in range(0, len(getSel)):
    cmds.setAttr( str(str(getSel[i])+".visibility"), 0, k = True)
    
#Loop through all objects setting Visibility to On, incrementally frame by frame and setting keys.    
for i in range(0, len(getSel)):
    cmds.currentTime(i)
    cmds.setAttr( str(str(getSel[i])+".visibility"), 1, k = True)
    cmds.setKeyframe()
    
