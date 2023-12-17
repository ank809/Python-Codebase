# Decorators are used to decorate a function
# Decorators are functions that take another function as input
# and return a new function with some modified behavior.

def greet(fx):
    def mfx():
        print('Good morning')
        fx()
        print('Thanks for using this function')

    return mfx


@greet
def hello():
    print("Hello Guys")


hello()


def wishes(fx):
    def wish():
        print('Merry Christmas')
        fx()

    return wish


@wishes
def thanks():
    print("Thank you for your wishes")


thanks()
