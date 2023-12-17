# Class is a blueprint or template for creating object
# Class defines the properties that a object may have. It consists of data members and member functions
# Object is an instance of a class and is used to access the members of the class
# Self keyword is used for referring to the object which you are currently calling
class Person:
    name="Ankita"
    age=19
    occupation="Software Developer"
    def info(self):
        print(self.name,"is", self.age, "years old and she is a",self.occupation)

a= Person()
a.info()
b=Person()
b.name="Astha"
b.age=21
b.occupation="IAS Officer"
b.info()