#write a python program to implement dictionary and its methods

#installing the dictionary in the program
d={1:'one', 2:'two', 3:'three'}
print(d)

print("\n")
#methods in dictionary

#items()
print(d.items())

#keys()
print(d.keys())

#values()
print(d.values())

#pop()
n = int(input("enter the key"))
print(d.pop(n))
print(d)

#popitem()
print(d.popitem())
print(d)

#get()
g=int(input("enter the key"))
print(d.get(g))

#copy()
a=d.copy()
print(a)

#fromkeys()
x={1,2,3,4}
y='num'
print(d.fromkeys(x,y))

#setdefault()
print(d.setdefault(3))
print(d.setdefault(5))
print(d.setdefault(6,'six'))
print(d)

#clear()
print(d.clear())

