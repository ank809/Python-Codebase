# Access Modifiers are used to restrict the access of the variables
# There's no such concept of access modifiers in python but we use it only for our convenience
# Public, Protected(_), Private(__)

class Student:
    def __init__(self, name, id):
        self.name= name
        self.__id= id

    def display(self):
        print(self.name, self.__id)

a= Student("Ankita", 1220)
a.display()
# print(a.__id) Cannot access it directly

print(a.__dir__())
print(a._Student__id)  #Can be accessed indirectly
# This is known as Name Mangling, and it is a technique used to protect class private member

class Greet:
    def __init__(self, message):
        self._message= message

    def display(self):
        print(self._message)
a=Greet("Hello , Good evening")
print(a._message)
