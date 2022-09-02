import math, random

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    pi = 3.1415
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
    def scale(self, v):
        self.x *= v
        self.y *= v

    @staticmethod
    def from_polar(r, theta): # static methods belong to the type, not the instance
        px = r * math.cos(theta)
        py = r * math.sin(theta)
        return Point(px, py)

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __repr__(self):
        return f'Point({self.x},{self.y})'

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y
    
    def __neq__(self, p):
        return self.x != p.x or self.y != p.y

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Index out of range!!!")

    def __len__(self):
        return 2

class RandomPoint(Point):
    def __helper_function(self):
        return random.randint(1,10)

    def __init__(self):
        self.x = self.__helper_function()
        self.y = self.__helper_function()

p1 = RandomPoint()
p2 = RandomPoint()
print(p1.x, p1.y)
print(p2.x, p2.y)

p3 = Point()
p4 = Point(4, 3)
p5 = Point(2, 10)

p3.distance(p2)

p4.scale(2)

print(p4.x, p4.y)

print(p3.pi)
print(p4.pi)

Point.pi = 3.2

print(p3.pi)
print(p4.pi)

p6 = Point.from_polar(1.414, Point.pi/4)
print(p6.x, p6.y)

print(p1._RandomPoint__helper_function())

print(len(p1))