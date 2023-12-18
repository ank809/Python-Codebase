# Unpacking is the process of assigning the tuple items as values to variables.
info = ("Ankita", 19, "Himachal Pradesh")
(name, age, state) = info
print("Name: ", name)
print("Age: ", age)
print("Hometown: ", state)

# If you have more tuple items than the variables then use * and the python will
# automatically match values to variables and assign to them

fauna1=("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals, bird, fish)= fauna1
print("Animals: ", animals)
print("Birds: ", bird)
print("Fish: ", fish)

fauna2 = ("parrot", "cat", "dog", "horse", "pig", "salmon")
(bird, *animals, fish) = fauna2
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)

fauna3 = ("parrot", "salmon", "cat", "dog", "horse", "pig")
(bird, fish, *animals) = fauna3
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)

