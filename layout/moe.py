import time
import win32api
import win32gui
import win32con
import win32clipboard
from .layout import Layout

class Moe(Layout):
    path = 'C:/Program Files/moe_2019.0102/bin/moe.exe'
    title = 'MOE 2019.0102'
    open_title = 'Open'
    load_title = 'Load PDB File'


    open_dir_pos = [575, 40]
    open_file_pos = [504, 341]
    load_ignore_water = [772 - 685, 592 - 332]
    load_ok = [765 - 685, 659 - 332]

    def launch(self):
        self.moe_win = win32gui.FindWindow(None, Moe.title)
        if self.moe_win == 0: win32api.ShellExecute(0, 'open', Moe.path, '', '', 1)
        while self.moe_win == 0:
            time.sleep(1)
            self.moe_win = win32gui.FindWindow(None, Moe.title)
        time.sleep(2) # 我还得等窗口渲染完成这个不是搞笑么
        win32gui.SetForegroundWindow(self.moe_win)
        self.moe_win_rect = win32gui.GetWindowRect(self.moe_win)

        return self
    
    def import_file(self, path, file):
        self._keybd([17, 79])

        while True:
            moe_open_win = win32gui.FindWindow(None, Moe.open_title)
            time.sleep(1)
            if moe_open_win != 0: break
        time.sleep(1) # 终于还是活成了自己最讨厌的样子
        left, top, right, bottom = win32gui.GetWindowRect(moe_open_win) # 526 304
        
        # 定位受体所在路径
        self._copy(path)
        if self.is_dev: time.sleep(1)
        self._move(left + self.open_dir_pos[0], top + self.open_dir_pos[1])._click()
        if self.is_dev: time.sleep(.5)
        self._dbclick()._paste()._enter()
        time.sleep(.5)

        # 定位受体文件
        self._copy(file)._paste()
        time.sleep(.5)
        self._enter()

        return self
    
    def ignore_water(self, flag = False):
        while True:
            moe_load_win = win32gui.FindWindow(None, Moe.load_title)
            time.sleep(1)
            if moe_load_win != 0: break
        time.sleep(1) # 何时才能终结这种屈辱
        left, top, right, bottom = win32gui.GetWindowRect(moe_load_win) # 685 332

        if flag: self._move(left + self.load_ignore_water[0], top + self.load_ignore_water[1])._click()
        if self.is_dev: time.sleep(1)
        self._move(left + self.load_ok[0], top + self.load_ok[1])._click()

        return self