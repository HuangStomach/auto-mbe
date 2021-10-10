import time
import win32api
import win32gui
import os
from .layout import Layout

class Data(Layout):
    title = 'DataView...'
    

    def launch(self):
        while True:
            self.win = win32gui.FindWindow(None, self.title)
            time.sleep(1)
            if self.win != 0 and win32gui.IsWindowEnabled(self.win): break
        self.rect = win32gui.GetWindowRect(self.win) # 200 16
        win32gui.SetForegroundWindow(self.win)

        return self