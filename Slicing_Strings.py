# You can return a range of characters by using the slice syntax.
b= "Hello World"
# 7 is not included
print(b[2:7])

# By default, it will start from 0
print(b[:7])

# It will go till end if end index is not specified
print(b[4:])

# Negative indexing

print(b[-1])   # ! is printed
print(b[-5: -2])

print(b.upper())
print(b.lower())
# To remove whitespaces
# Strip removes whitespaces from beginning and end
print(b.strip())

# To split a string into 2 substring
print(b.split(' '))  # return ['Hello', 'World!']
print(b.center(20))

print(b.encode())

print(b.isalpha())
# it returns the last index where the character is found
print(b.rfind('l'))
# it adds 0's in the beginning till the string reaches the desired length
# if the length of the value is less than length of string then no filling is done
print(b.zfill(5))  # length is less than actual length so no filling is done
print(b.zfill(12))