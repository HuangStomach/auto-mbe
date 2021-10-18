import time
import win32api
import win32gui
import win32con

while True:
    time.sleep(1)
    print(win32api.GetCursorPos())
# while True:
#     time.sleep(1)
#     pop = win32gui.FindWindow('wtPopupWindowClass', None)
#     text = win32gui.GetWindowText(pop)
#     print(win32api.SendMessage(pop, win32con.WM_GETTEXTLENGTH))
#     print(text)

# 4.5 4.3