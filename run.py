import time
import win32gui
import win32con

moe = win32gui.FindWindow(None, 'MOE 2019.0102')
time.sleep(3)
win32gui.SendMessage(moe, win32con.WM_CLOSE)