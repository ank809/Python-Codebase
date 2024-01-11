"""
*args : Arbitrary arguments
**kwargs: Keyword arguments
 """

nums= [2, 3, 4, 5, 6]
print(nums)
# unpacking : if * is used before lists and dict it unoacks it
print(*nums)

def pizza(size, *toppings, **details):
    print(f"The size of pizza is {size} and topings are {toppings}")
    for topping in toppings:
        print(topping)
    # prints as a dictionary
    print(details)
    for key, values in details.items():
        print(key,":",values)
pizza("large", "pepperoni", "olives", "chilli flakes", delivery=True, tip=5)