#Simple Loop For Writing Out VDBs In Custom Setups.

import maya.cmds as cmds

fStart = 0
fEnd   = 120

for i in range(fStart, fEnd):
    cmds.currentTime(i)
    cmds.setAttr("OpenVDBWrite.VdbFilePath", 'X:/Frame.'+(i.zfill(3))+"001.vdb', type="string")
