import time
import win32api

while True:
    time.sleep(1)
    print(win32api.GetCursorPos())