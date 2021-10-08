import sys, getopt
import win32api
import win32gui
import win32con
import win32clipboard

class Layout:
    is_dev = True
    def __init__(self) -> None:
        opts, args = getopt.getopt(sys.argv[1:], '', ['dev='])
        for opt, arg in opts:
            if opt == '--dev' and arg == 'false': self.is_dev = False

    def _move(self, x, y):
        if not self.is_dev: win32api.SetCursorPos([x, y])
        return self

    def _click(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        return self
    
    def _dbclick(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        return self

    def _keybd(self, keys):
        if isinstance (keys, list):
            for key in keys: win32api.keybd_event(key, 0, 0 ,0)
            for key in keys: win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
        else:
            win32api.keybd_event(keys, 0, 0 ,0)
            win32api.keybd_event(keys, 0, win32con.KEYEVENTF_KEYUP, 0)
        return self
    
    def _copy(self, text):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text, win32con.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        return self
    
    def _paste(self):
        self._keybd([17, 86])
        return self
    
    def _enter(self):
        self._keybd(13)
        return self