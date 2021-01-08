#Simple Loop For Writing Out VDBs In Custom Setups.

import maya.cmds as cmds

for i in range(0, 140):
    cmds.currentTime(i)
    cmds.setAttr("OpenVDBWrite.VdbFilePath", 'X:/Frame.'+(i.zfill(3))+"001.vdb', type="string")
