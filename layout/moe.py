import time
import win32api
import win32gui
import os
from .layout import Layout

class Moe(Layout):
    # path = 'C:/Program Files/moe_2019.0102/bin/moe.exe'
    path = 'D:/moe_2019.0102/bin/moe.exe'
    title = 'MOE 2019.0102'
    rect = []
    # seq
    seq_title = 'Sequence Editor'
    seq_edit_pos = [44, 762]
    seq_tag_pos = [49, 789]
    seq_rename_pos = [86, 1000]
    seq_ok_pos = [299 + 6, 565 - 524]
    # save
    save_title = "Save"
    save_dir_pos = [1321, 469]
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
        self._keybd([17, 81])
        while True:
            moe_seq_win = win32gui.FindWindow(None, self.seq_title)
            time.sleep(1)
            if moe_seq_win != 0 and win32gui.IsWindowEnabled(moe_seq_win): break
        
        self.import_file(path, file, ignore_water, ext)
        self.ignore_water(ignore_water)
        time.sleep(1)
        
        self._move(self.seq_edit_pos)._click()
        if self.is_dev: time.sleep(1)
        self._move(self.seq_rename_pos)._click()

        self._copy(type)\
            ._keybd([17, 65])\
            ._paste()\
            ._enter()
        
        self._keybd([17, 83])
        while True:
            moe_save_win = win32gui.FindWindow(None, self.save_title)
            time.sleep(1)
            if moe_save_win != 0 and win32gui.IsWindowEnabled(moe_save_win): break
        
        # 定位受体所在路径
        if self.is_dev: time.sleep(1)
        self._copy(path)\
            ._move(self.save_dir_pos)\
            ._click()
        time.sleep(1)
        self._keybd([17, 65])\
            ._paste()\
            ._enter()

        time.sleep(1)
        if os.path.exists(path + file + '.moe'): os.remove(path + file + '.moe') # 删除旧文件
        # 定位受体文件
        self._copy(file)\
            ._paste()
        time.sleep(1)
        self._enter()

        self.delete()

        return self

    def delete(self):
        self._keybd([17, 81])
        while True:
            moe_seq_win = win32gui.FindWindow(None, self.seq_title)
            time.sleep(1)
            if moe_seq_win != 0 and win32gui.IsWindowEnabled(moe_seq_win): break

        self._move(self.seq_tag_pos)._click()
        
        self._keybd(46)
        while True:
            moe_delete_win = win32gui.FindWindow(None, self.delete_title)
            time.sleep(1)
            if moe_delete_win != 0 and win32gui.IsWindowEnabled(moe_delete_win): break
        time.sleep(1)
        self._move(self.delete_ok_pos)._click()

        return self
    
    def import_file(self, path, file, ignore_water = False, ext='.moe'):
        self._keybd([17, 79])

        while True:
            moe_open_win = win32gui.FindWindow(None, self.open_title)
            time.sleep(1)
            if moe_open_win != 0 and win32gui.IsWindowEnabled(moe_open_win): break
        left, top, right, bottom = win32gui.GetWindowRect(moe_open_win) # 526 304
        win32gui.SetActiveWindow(moe_open_win)
        
        # 定位受体所在路径
        if self.is_dev: time.sleep(1)
        self._copy(path)\
            ._move(left + self.open_dir_pos[0], top + self.open_dir_pos[1])\
            ._click()
        time.sleep(1)
        self._keybd([17, 65])\
            ._paste()\
            ._enter()

        time.sleep(1)
        # 定位受体文件
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