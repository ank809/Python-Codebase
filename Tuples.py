# Tuples are ordered collection of data items. They store multiple items in a single variable.
# Tuple items are separated by commas and enclosed within round brackets ().
# Tuples are unchangeable meaning we can not alter them after creation.

tuple1= (2, 4, 5, 7, 8)
print(tuple1[0])
print(tuple1)
# tuple1[0]=10 This will give error as we can;t modify tuples
print(tuple1)

country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")

print(tuple1[2:5])
print(tuple1[-5:-1])

# printing every 3rd consecutive withing given range

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[2:9:3])

# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list.
# Then perform operation on that list and convert it back to tuple.

countries=("Japan", "South Korea", "Finland", "India", "England", "Germany", "Europe")
temp= list(countries)
temp.append("America")
print(temp)
print(temp.pop())
print(temp)
temp[0]="Thailand"
print(temp)
print(countries)
countries= tuple(temp)
print(countries)

# we can directly concatenate two tuples instead of converting them to list and back.
country1= ("Pakistan", "Afghanistan", "Italy", "Russia")
country2= ("UAE", "China", "Taliban")
country= country1+country2
print(country)