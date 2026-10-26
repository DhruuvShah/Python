"""Demonstrate polygon area calculation using triangle, rectangle, and square subclasses."""

class Polygon:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Traingle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [
    Traingle(10,6),
    Rectangle(8,4),
    Square(5)
]

for shape in shapes:
    print(type(shape).__name__,"Area:", shape.area())
