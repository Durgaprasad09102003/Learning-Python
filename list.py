#write a python program to implement list and its methods

#installing the list in the program
list1=list(map(int, input("enter the elements").split(",")))
print("the list is", list1)

print("\n")
#methods in list

#index()
a=int(input('enter the element to check find the index'))
print("the output for index function is", list1.index(a))

#append()
b=int(input('enter the element to append'))
list1.append(b)
print("the output for append function is", list1)

#insert()
c=int(input("enter the index for insert in list"))
d=int(input("enter the element for insert in list"))
list1.insert(c, d)
print("the output for insert function is", list1)

#copy()
print("the output for copy function is", list1.copy())

#extend()
list2=list(map(int,input("enter the elements for extend function[list2] ").split(",")))
print("the list for extend function is", list1)
list1.extend(list2)
print("the output for extend function is", list1)

#count()
e=int(input("enter the elements to count in list"))

print("the output for count function is", list1.count(e))

#pop()
b=int(input("enter the elements to pop in list"))
list1.pop(b)
print("the output for pop function is", list1)

#remove()
b=int(input('enter the elements to remove in list'))
list1.remove(b)
print("the output for remove function is", list1)

#sort()
list1.sort()
print("the output for sort function is", list1)

#reverse()
list1.reverse()
print("the output for reverse function is", list1 )

#clear()
list1.clear()
print("the output for clear function is", list1)

