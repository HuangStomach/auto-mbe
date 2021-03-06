import time
import win32api
import win32gui
import os
from .layout import Layout
from .seq import Seq

class Moe(Layout):
    # path = 'C:/Program Files/moe_2019.0102/bin/moe.exe'
    path = 'D:/moe_2019.0102/bin/moe.exe'
    title = 'MOE 2019.0102'
    rect = []
    # open
    open_title = 'Open'
    open_dir_pos = [540, 40]
    open_file_pos = [504, 341]
    # delete
    delete_title = 'Delete Chains'
    delete_ok_pos = [1200, 752]
    # load
    load_title = 'Load PDB File'
    load_ignore_water = [1218 - 1125, 789 - 521]
    load_ok = [1205 - 1125, 860 - 521]
    # compute
    compute_pos = [547, 65]
    # dock
    dock_title = 'Dock'
    dock_pos = [585, 236]
    dock_receptor_pos = [1410, 488]
    dock_receptor_item_pos = [1369, 667]
    dock_ligandr_pos = [1305, 583]
    dock_ligandr_item_pos = [1313, 686]
    dock_run_pos = [1059, 937]

    def launch(self):
        self.moe_win = win32gui.FindWindow(None, self.title)
        if self.moe_win == 0: win32api.ShellExecute(0, 'open', self.path, '', '', 1)
        while True:
            self.moe_win = win32gui.FindWindow(None, self.title)
            time.sleep(1)
            if self.moe_win != 0 and win32gui.IsWindowEnabled(self.moe_win): break
        self.rect = win32gui.GetWindowRect(self.moe_win) # 200 16
        win32gui.SetForegroundWindow(self.moe_win)

        return self

    def transform(self, path, file, type, ignore_water = False, ext='.pdb'):
        seq = Seq()
        seq.launch()
        
        self.import_file(path, file, ignore_water, ext)
        self.ignore_water(ignore_water)
        time.sleep(1)
        
        seq.rename(type)\
            .save(path, file)\
            .delete()

        return self

    def delete(self):
        seq = Seq()
        seq.launch()\
            .delete()

        return self
    
    def import_file(self, path, file, ignore_water = False, ext='.moe'):
        self._keybd([17, 79])

        while True:
            moe_open_win = win32gui.FindWindow(None, self.open_title)
            time.sleep(1)
            if moe_open_win != 0 and win32gui.IsWindowEnabled(moe_open_win): break
        left, top, right, bottom = win32gui.GetWindowRect(moe_open_win) # 526 304
        win32gui.SetActiveWindow(moe_open_win)
        
        # ????????????????????????
        if self.is_dev: time.sleep(1)
        self._copy(path)\
            ._move(left + self.open_dir_pos[0], top + self.open_dir_pos[1])\
            ._click()
        time.sleep(1)
        self._keybd([17, 65])\
            ._paste()\
            ._enter()

        time.sleep(1)
        # ??????????????????
        self._copy(file + ext)\
            ._paste()
        time.sleep(1)
        self._enter()

        return self
    
    def ignore_water(self, flag = False):
        while True:
            moe_load_win = win32gui.FindWindow(None, self.load_title)
            time.sleep(1)
            if moe_load_win != 0 and win32gui.IsWindowEnabled(moe_load_win): break
        left, top, right, bottom = win32gui.GetWindowRect(moe_load_win) # 685 332
        
        if flag: self._move(left + self.load_ignore_water[0], top + self.load_ignore_water[1])._click()
        time.sleep(1)
        self._move(left + self.load_ok[0], top + self.load_ok[1])\
            ._click()

        return self
    
    def dock(self):
        self._move(self.compute_pos)._click()
        time.sleep(1)
        self._move(self.dock_pos)._click()
        while True:
            moe_dock_win = win32gui.FindWindow(None, self.dock_title)
            time.sleep(1)
            if moe_dock_win != 0 and win32gui.IsWindowEnabled(moe_dock_win): break
        self._move(self.dock_receptor_pos)._click()
        self._move(self.dock_receptor_item_pos)._click()
        self._move(self.dock_ligandr_pos)._click()
        self._move(self.dock_ligandr_item_pos)._click()
        self._move(self.dock_run_pos)._click()
        
        return self