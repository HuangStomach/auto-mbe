import time
import win32api
import win32gui
import win32con
import win32clipboard
from .layout import Layout

class Moe(Layout):
    path = 'C:/Program Files/moe_2019.0102/bin/moe.exe'
    title = 'MOE 2019.0102'
    rect = []
    # seq
    seq_title = 'Sequence Editor'
    seq_edit_pos = [43 + 6, 566 - 524]
    seq_tag_pos = [47 + 6, 594 - 524]
    seq_rename_pos = [83 + 6, 792 - 524]
    seq_ok_pos = [299 + 6, 565 - 524]
    # open
    open_title = 'Open'
    open_dir_pos = [575, 40]
    open_file_pos = [504, 341]
    # load
    load_title = 'Load PDB File'
    load_ignore_water = [772 - 685, 592 - 332]
    load_ok = [765 - 685, 659 - 332]
    # compute
    compute_pos = [438 - 200, 57 - 16]
    # dock
    dock_title = 'Dock'
    dock_pos = [475 - 200, 228 - 16]
    dock_receptor_pos = [960 - 536, 297 - 275]

    def launch(self):
        self.moe_win = win32gui.FindWindow(None, self.title)
        if self.moe_win == 0: win32api.ShellExecute(0, 'open', self.path, '', '', 1)
        while True:
            self.moe_win = win32gui.FindWindow(None, self.title)
            time.sleep(1)
            if self.moe_win != 0 and win32gui.IsWindowEnabled(self.moe_win): break
        self.rect = win32gui.GetWindowRect(self.moe_win) # 200 16
        win32gui.SetForegroundWindow(self.moe_win)
        self.moe_win_rect = win32gui.GetWindowRect(self.moe_win)

        return self

    def transform(self, path, file, type, ignore_water = False):
        self._keybd([17, 81])
        while True:
            moe_seq_win = win32gui.FindWindow(None, self.seq_title)
            time.sleep(1)
            if moe_seq_win != 0 and win32gui.IsWindowEnabled(moe_seq_win): break
        left, top, right, bottom = win32gui.GetWindowRect(moe_seq_win) # -6 524 1672 1017
        
        self.import_file(path, file, ignore_water)
        
        self._move(left + self.seq_edit_pos[0], top + self.seq_edit_pos[1])._click()
        if self.is_dev: time.sleep(1)
        self._move(left + self.seq_rename_pos[0], top + self.seq_rename_pos[1])._click()

        self._copy(type)\
            ._paste()\
            ._enter()

        return self

    
    def import_file(self, path, file, ignore_water = False):
        self._copy(path)
        self._keybd([17, 79])

        while True:
            moe_open_win = win32gui.FindWindow(None, self.open_title)
            time.sleep(1)
            if moe_open_win != 0 and win32gui.IsWindowEnabled(moe_open_win): break
        left, top, right, bottom = win32gui.GetWindowRect(moe_open_win) # 526 304
        win32gui.SetActiveWindow(moe_open_win)
        
        # 定位受体所在路径
        if self.is_dev: time.sleep(1)
        self._move(left + self.open_dir_pos[0], top + self.open_dir_pos[1])\
            ._click()\
            ._keybd([17, 65])\
            ._paste()\
            ._enter()

        time.sleep(1)
        # 定位受体文件
        self._copy(file)\
            ._paste()
        time.sleep(1)
        self._enter()

        self.ignore_water(ignore_water)

        return self
    
    def ignore_water(self, flag = False):
        while True:
            moe_load_win = win32gui.FindWindow(None, self.load_title)
            time.sleep(1)
            if moe_load_win != 0 and win32gui.IsWindowEnabled(moe_load_win): break
        left, top, right, bottom = win32gui.GetWindowRect(moe_load_win) # 685 332

        if flag: self._move(left + self.load_ignore_water[0], top + self.load_ignore_water[1])._click()
        if self.is_dev: time.sleep(1)
        self._move(left + self.load_ok[0], top + self.load_ok[1])\
            ._click()

        return self
    
    def dock(self):
        self._move(self.rect[0] + self.compute_pos[0], self.rect[1] + self.compute_pos[1])._click()
        if self.is_dev: time.sleep(1)
        self._move(self.rect[0] + self.dock_pos[0], self.rect[1] + self.dock_pos[1])._click()
        while True:
            moe_dock_win = win32gui.FindWindow(None, self.dock_title)
            time.sleep(1)
            if moe_dock_win != 0 and win32gui.IsWindowEnabled(moe_dock_win): break
        left, top, right, bottom = win32gui.GetWindowRect(moe_dock_win) # 536 275
        self._move(left + self.dock_receptor_pos[0], top + self.dock_receptor_pos[1])._click()
        
        return self