""" Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
 """

mylist = ["Apple", "Banana", "Orange", "Mango"]
print(mylist)
print(mylist[0])
print(len(mylist))
# List can contain different datatypes
mylist1 = [1, 3.7, 3j, "Astha"]
print(mylist1)
print(type(mylist))

newlist = list(('Ankita', 2, 7.9, 6j))
print(newlist)
newlist1 = set(('Ankita', 2, 7.9, 6j))
print(newlist1)
newlist2 = tuple(('Ankita', 2, 7.9, 6j))
print(newlist2)

print(mylist[2:4])

print(mylist1[:4])

print(newlist[2:])

if "Banana" in mylist:
    print("Yes, Banana is present")
else:
    print("No, Banana is not present")

list1 = ["hello", "hi", 'hey', 1, 2]
print(list1)
list1.remove(1)
# lis1.remove(2)
print(list1)
print(list1.pop())
list1.reverse()
print(list1)