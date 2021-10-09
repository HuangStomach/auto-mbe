import time
import win32api
import win32gui
import win32con
import win32clipboard
from layout.moe import Moe
from source.DTINet import DTINet

moe = Moe()
moe.launch()

dtinet = DTINet()
for receptor in dtinet.receptor():
    #moe.import_file(dtinet.path, receptor, ignore_water=True)
    for ligand in dtinet.ligand():
        time.sleep(1) # 给渲染一点时间
        #moe.import_file(dtinet.path, ligand)
        moe.transform(dtinet.path, ligand, type='ligand')
