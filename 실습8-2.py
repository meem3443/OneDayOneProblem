from operator import length_hint


class Box:
    def __init__(self, length, height, depth):
        self.length = length
        self.height = height
        self.depth = depth

    def __str__(self):
        return (f"가로 :{self.length}, 세로 :{self.height}, 높이 :{self.depth}")

    def  setLength(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def  setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def  setdepth(self, depth):
        self.depth = depth

    def getdepth(self):
        return self.depth

box1 = Box(10, 5, 3)

print(box1)

print("상자의 부피는", box1.getHeight() * box1.getLength() * box1.getdepth())

