# Functions  are block of statements that is used to perform a specified task
# def keyword is used to define function in python
# if ypu want to give body to a function later on you can use pass keyword
a= 10
b=20
# gmean= (a*b)/a+b
# print(gmean)

def gmean(a, b):
    gmean= (a*b)/(a+b)
    print(gmean)

gmean(a,b)
gmean(14,17)
gmean(10,2)

def isGreater(a, b):
    if(a>b):
        print(a,"is greater")
    else:
        print(b, 'is greater ')

isGreater(14,78)

def isLesser(a,b):
    pass