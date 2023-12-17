""" Constructor is special function which do not have return type and is called automatically when an
object of a class is created. It is used to initialize and create object of a class
Two types of constructor:
1. Default Constructor : It doesn't take any arguments and is called automatically you do not need to initialize it
2. Parameterized Constructor: It takes arguments
 def __init() is used to define a constructor
Self is a parameter is  passed automatically
You cannot have multiple constructors in python and if you do so then the last defined one will override the
previous one """

class Student:
    # def __init__(self):
    #     print("This is default constructor")
    def __init__(self, a, b, c):
        self.name= a
        self.age=b
        self.r_no=c
        print("This is parameterized Constructor")
    def info(self):
        print(self.name, self.age, self.r_no)

a= Student("Ankita", 12, 12202002)
b=Student("Astha", 1, 12201605)
a.info()
b.info()