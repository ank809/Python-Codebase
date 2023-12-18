# When we have function with same name in both parent and child class then the child class func overrides the base class
# fun

# When a class have more than one func with same name but different args is : Method Overloading

class Shape :
    def __init__(self, a):
        self.a= a
    def shapes(self):
        print("I am in shape class ")
    def area(self):
        return self.a*self.a

class Rectangle(Shape):

    def __init__(self, l, b):
        self.l=l
        self.b=b


#  Overrides method in Shape
    def area(self):
        return self.l*self.b

 #  Overrides method in Shape
    def shapes(self):
        print("I am in Rectangle class ")


a= Shape(2)
print(a.area())
a.shapes()

b= Rectangle(2,4)
print(b.area())
b.shapes()