# There are three numeric types in Python
''' int: Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
float: Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
z = -87.7e100
complex: Complex numbers are written with a "j" as the imaginary part:
x=3+5j
'''

# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))