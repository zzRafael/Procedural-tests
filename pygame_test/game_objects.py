# game_objects.py

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pos = (self.x, self.y)
        self.size = 20

    def update(self):
        pass

class Planet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.size = 20

class Line:
    def __init__(self, start, end, color):
        self.start = start
        self.end = end
        self.color = color