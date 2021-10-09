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
    #moe.transform(dtinet.path, receptor, type='receptor', ignore_water=True)
    for ligand in dtinet.ligand():
        #moe.transform(dtinet.path, ligand, type='ligand')

        # moe.import_file(dtinet.path, ligand)
        # time.sleep(1)
        # moe.import_file(dtinet.path, receptor)
        # moe.dock()

        # moe.delete()
        time.sleep(2)
        win32gui.CloseWindow()
