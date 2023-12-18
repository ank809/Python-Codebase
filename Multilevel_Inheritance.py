# When a derived class inherits from another derived class

class Animal:
    def __init__(self, name, species):
        self.name= name
        self.species=species
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, "Dog")
        self.breed=breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed is {self.breed}")

class Golden_Retriever(Dog):

    def __init__(self, name ,color):
        Dog.__init__(self, name, "Golden Retriever")
        self.color=  color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color is {self.color}")

a= Golden_Retriever("Jojo", "Golden")
a.show_details()