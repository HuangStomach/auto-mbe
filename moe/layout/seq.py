import time
import win32api
import win32gui
import os
from .layout import Layout

class Seq(Layout):
    title = 'Sequence Editor'
    tag_pos = [49, 789]
    # delete
    delete_title = 'Delete Chains'
    delete_ok_pos = [1200, 752]
    # edit
    edit_pos = [44, 762]
    rename_pos = [86, 1000]
    # save
    save_title = "Save"
    save_dir_pos = [1321, 469]
    
    def launch(self):
        self._keybd([17, 81]) # ctrl + q
        while True:
            seq_win = win32gui.FindWindow(None, self.title)
            time.sleep(1)
            if seq_win != 0 and win32gui.IsWindowEnabled(seq_win): break

        return self

    def save(self, path, file):
        self._keybd([17, 83]) # ctrl + s
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

        return self

    def delete(self):
        self._move(self.tag_pos)._click()
        
        self._keybd(46) # delete
        while True:
            delete_win = win32gui.FindWindow(None, self.delete_title)
            time.sleep(1)
            if delete_win != 0 and win32gui.IsWindowEnabled(delete_win): break
        time.sleep(1)
        self._move(self.delete_ok_pos)._click()

        return self
    
    def rename(self, type):
        self._move(self.edit_pos)._click()
        self._move(self.rename_pos)._click()

        self._copy(type)\
            ._keybd([17, 65])\
            ._paste()\
            ._enter()

        return self