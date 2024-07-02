#write a python program to implement tuples and its methods

#installing the tuples in the program

tuple1=tuple(input("enter the elements").split(","))
print(tuple1)

print("\n")
#methods in tuples

#index()
a=input('enter the element to check the index')
print("the output for index function is", tuple1.index(a))

#count()
b=input('enter the element for count function')
print("the output for count function is", tuple1.count(a))


#len()
print("the output for count function is", len(tuple1))

#max()
print("the output for max function is", max(tuple1))

#min()
print("the output for min function is", min(tuple1))

#sorted()
print("the output for sorted function is", sorted(tuple1))


#delete()
del tuple1