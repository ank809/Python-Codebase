# We take input using input() in python
# And all the input we take is of type string

x = input('Enter your name: ')
# print(x)
#
a = input('Enter first number: ')
b = input('Enter second number: ')
# this will join the numbers as they are strings
print(a + b)
# this will give error as  we cannot divide or multiply strings (unsupported operand type(s) for /: 'str' and 'str' )
# print(a/b)
# print(a*b)
print(int(a) + int(b))
print(int(a) / int(b))
print(int(a) * int(b))

c = int(input('Enter first number: '))
d = int(input('Enter second number: '))
print(c + d)
print(float(c) + int(d))

# / operator always give floating value as output
print(c / d)
print(c * d)