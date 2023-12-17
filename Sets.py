# Sets are unordered, unchangeable , and do not allow duplicate members
# Sets can store var of different types
# True,1 and False 0 are treated as duplicate values

set1 = {'Hello', 'Anneyong Haseyo', 'Gamshamida', 'Saranghae'}
print(set1)
if 'Hello' in set1:
    print("Hello developers")
else:
    print('Bye developers')

print(type(set1))
print(len(set1))

set2 ={True, 1, False, 0}
print(set2)

list1 = ['Apple', 'Banana', 'Mango', 'Orange']

set3 = {'Kiwi', 'Watermelon'}
print(set3)
set3.update(list1)

print(set3)
set3.add('Cherry')
print(set3)

'''
Note: If the item to remove does not exist, remove() will raise an error.
Note: If the item to remove does not exist, discard() will NOT raise an error
 '''
set3.remove('Banana')
print(set3)

set3.discard('Apple')
set3.discard('Hi')
print(set3)

# Pops random element
print(set1.pop())

# del delete the set completely
del set2
# clear clears the set
set1.clear()

print(set1)

''' Join Sets
1. Union: keep all except duplicates
2. Update:keep all except duplicates
3. Intersection: keep only duplicates
'''

set4 = {'Hi', 'Namaste', 'AslaimWalikumn','Satsriakal' }
set5 ={'Bonjour', 'Anneyong Haseyo', 'Hi'}

# update method adds the items to sets
set4.update(set5)
print(set4)
# union() method  returns a new set containing all items from both sets
set7 = set4.union(set5)
print(set7)
set4.intersection_update(set5)
print(set4)