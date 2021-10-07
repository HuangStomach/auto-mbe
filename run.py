import time
import win32api
import win32gui
import pyautogui
from config import Moe

moe_win = win32gui.FindWindow(None, Moe.title)
if moe_win == 0: win32api.ShellExecute(0, 'open', Moe.path, '', '', 1)
while moe_win == 0:
    time.sleep(1)
    moe_win = win32gui.FindWindow(None, Moe.title)
win32gui.BringWindowToTop(moe_win)
left, top, right, bottom = win32gui.GetWindowRect(moe_win)
moe = Moe(left, top, right, bottom)
pyautogui.moveTo(moe.file()[0], moe.file()[1])

#time.sleep(3)
#win32gui.SendMessage(moe, win32con.WM_CLOSE)
