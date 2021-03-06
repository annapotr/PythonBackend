
class Point:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y


class Line:
    x1: float
    y1: float
    x2: float
    y2: float

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get(self):
        return self.x1, self.x2, self.y1, self.y2
