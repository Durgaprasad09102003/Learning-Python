from functools import *

list1 = list(map(int,input("enter the elements").split(" ")))
print(list1)

def add1(x, y):
    return(x+y)

print(reduce(add1,list1))
