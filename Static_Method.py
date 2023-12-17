# Static methods are used when we want to call the func without using objects
class Math:
    def __init__(self, a):
        self.a = a

    def addtoa(self, b):
        self.a = self.a + b

    @staticmethod
    def add(a, b):
        return a + b


a = Math(5)

a.addtoa(2)
print(a.a)
# Can't call the be;low function like this as it is not static so we need to have a ref var to it
# print(Math.addtoa(5))
print(Math.add(4, 5))
