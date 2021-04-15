class MyPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setx(self, x):
        self.x = x
    def sety(self, y):
        self.y = y
    def get(self):
        return self.x, self.y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy


mypnt = MyPoint(3, 4)
print(f"{mypnt.x}, {mypnt.y}")
print(f"{mypnt.get()}")
