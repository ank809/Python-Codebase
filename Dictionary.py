'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

# Dictionaries are used to store data values in key:value pairs.

mydic= {
    "brand":"Ford",
    "model":"Mustang",
    "year":2002,
}

print(mydic)
print(mydic["year"])
print(mydic["model"])

# can't have duplicate values in dictionary
mydic1= {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964,
    # "year": 2020,  # duplicate value overwrites existing values
}
print(mydic1["year"])
print(len(mydic1))

x= mydic.keys()
y=mydic1.values()
print(x)
print(y)

# items() method will return each item in a dictionary, as tuples in a list.
a= mydic1.items()
print(a)

if "Brand" in mydic1:
    print("Brand exists in mydic1")
else:
    print("Brand does not exist")

mydic1["color"]="red";
print(mydic1)

# Update dictionaries
mydic1["brand"]="Lamborghini"
print(mydic1)

mydic1.update({"brand": "Ferrari"})
print(mydic1)

print(mydic1.pop("brand"))

print(mydic1.popitem())

# The del keyword can also delete the dictionary completely:
del mydic1['year']

print(mydic1)

# clear empties the dictionary
mydic1.clear()
print(mydic1)