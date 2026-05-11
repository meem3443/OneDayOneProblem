class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"좌표 : {self.x}, {self.y}, 너비 : {self.width}, 높이 : {self.height}"
        
    def setX(self, x):
        self.x = x
        
    def getX(self):
        return self.x
    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y
    def setW(self, width):
        self.width = width

    def getW(self):
        return self.width
    def setH(self, height):
        self.height = height

    def getH(self):
        return self.height
    
    def getArea(self, x, y):
        
        return self.x * self.y
    
    def overlap(self, r):
        if self.x < r.x + r.width and self.x + self.width > r.x and self.y < r.y + r.height and self.y + self.height > r.y:
            return True
        else:
            return False
        
r1 = Rectangle(0, 0, 10, 10)
r2 = Rectangle(5, 5, 10, 10)
print(r1)
print(r2)
print(r1.overlap(r2))
    
    