# Strings in python are surrounded by either single quotation marks, or double quotation marks.
#   There is no character datatype in python
# A single character is simply a string of length 1

a="Ankita"
print(a)
print(a[4])

# Looping through strings
for i in "Ankita":
    print(i)

# Length of a string
print("Length of a is ",len(a))

# To check if string is present or not
# IN
a= "My name is Ankita and I am a Computer Science student."
print("Computer" in a)   #This will print true as computer is present in a
print('Thakur' in a)   #False

# Print only if Ankita is present in a
if "ankita " in a:
    print("Ankita is present")
else:
    print('Ankita is not present')

# NOT IN
print("ASTHA" not in a)
if "ASTHA" not in a:
    print("ASTHA IS NOT PRESENT")
else:
    print('ASTHA IS PRESENT')
    