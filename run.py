import time
import win32api
import win32gui
import win32con
import win32clipboard
from layout.moe import Moe
from source.Temp import Temp

moe = Moe()
moe.launch()

handler = Temp()
for receptor in handler.receptor():
    #moe.transform(handler.path, receptor, type='receptor', ignore_water=True)
    for ligand in handler.ligand():
        #moe.transform(handler.path, ligand, type='ligand')

        # moe.import_file(handler.path, ligand)
        # time.sleep(1)
        # moe.import_file(handler.path, receptor)
        # moe.dock()

        # moe.delete()
        time.sleep(2)
        win32gui.CloseWindow()
