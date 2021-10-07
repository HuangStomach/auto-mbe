class Moe:
    path = 'C:/Program Files/moe_2019.0102/bin/moe.exe'
    title = 'MOE 2019.0102'
    _file_pos = [22, 40] # left top

    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
    
    def file(self):
        return [self.left + self._file_pos[0], self.top + self._file_pos[1]]