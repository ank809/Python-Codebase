class Animal:
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed

    def make_sound(self):
        print("Sound made by the animal!")

    def eats(self, food):
        self.food= food
        print(f"{self.name} eats {self.food}")

class Cat(Animal):
    def __init__(self, name , breed):
        super().__init__(name, breed)

    def make_sound(self):
        print("Meow Meow!")

    def eats(self):
        print("Cat drinks milk")

a= Animal("Dog", "Husky")
a.make_sound()
a.eats("Wheat")

b= Cat("Cat", "Cat")
b.eats()
b.make_sound()