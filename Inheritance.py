""" Inheritance : when a class is derived from other class. The new class is child class, and it inherits all the
public and protected members of that class and also define some of its own.
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hybrid Inheritance
5. Hierarchical Inheritance """

class Employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id

    def showDetails(self):
        print("The name of Employee is ", self.name , "and id is", self.id)

class Programmer(Employee):
    def __init__(self, name, id, occ):
        super().__init__(name, id)
        self.occ=occ

    def showinfo(self):
        print("Occupation is", self.occ)


a= Employee("Ankita", 400)
a.showDetails()

b= Employee("Astha", 23)
b.showDetails()
# b.showinfo() can't use because base class cannot access derived class members

c= Programmer("Harsh", 14, "Software Developer")
c.showDetails()
c.showinfo()