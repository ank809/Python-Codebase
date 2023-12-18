import math

class Shape:
    def __init__(self, x, type):
        self.x = x
        self.type = type

    def area(self):
        return 3.14 * self.x * self.x

class TwoDimensionalShape(Shape):
    def __init__(self, x):
        Shape.__init__(self, x, "Two Dimensional Shape")

    def perimeter(self):
        print("The perimeter function in the TwoDimensionalShape class")

class Circle(TwoDimensionalShape):
    def __init__(self, x):
        TwoDimensionalShape.__init__(self, x)

    def circumference(self):
        print("Circumference is", 2 * math.pi * self.x)

class Cylinder(Circle):
    def __init__(self, x, h):
        Circle.__init__(self, x)
        self.h = h

    def volume(self):
        print(f"Volume of cylinder is {math.pi * self.x * self.x * self.h}")

a = Circle(2)
a.area()
a.perimeter()
a.circumference()

b = Cylinder(3, 8)
b.area()
b.perimeter()
b.circumference()
b.volume()
