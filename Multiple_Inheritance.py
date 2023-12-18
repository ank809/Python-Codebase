# When a class is derived from more than one classes
# When a class have more than one parent class

class Employee:
    def __init__(self, name):
        self.name= name

    def show(self):
        print(f"The name of the employee is {self.name}")

class Dancer:

    def __init__(self, dance):
        self.dance=dance

    def show(self):
        print(f"The dance is {self.dance}")

# class DancerEmployee(Employee, Dancer):
class DancerEmployee( Dancer, Employee):  # the class which we write earlier will have higher priority and the
                                             #  functions of that will be called if we have func of same name in
                                             # both the classes
    def __init__(self, name, dance):
        self.name=name
        self.dance=dance


a= DancerEmployee("Ankita", "Kathak")
a.show()

