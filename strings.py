#write a python program to implement the strings and its operations

#installing the string in the program 
str=input("enter the string\t")
print("the string is", str)

print("\n")
#operations of strings
print('operations of strings')
print("\n")

str1=input("enter the string for function\t")
#capitalize()

print("the string is", str1)
print("the output for capitalize function is", str1.capitalize())

print("\n")

#count()
a=input("enter the string to check for the count function")
print("the output for count function is", str1.count(a))

print("\n")

#endswith()
b=input("enter the string to check for the endswith function")
print("the output for endswith function is", str1.endswith(b))

print("\n")

#find()
c=input("enter the string to check for the find function")
print("the output for find function is", str1.find(c))

print("\n")

#isalnum()
print("the output for isalnum function is", str1.isalnum())

print("\n")

#isidentifier()
print("the output for isidentifier function is", str1.isidentifier())

print("\n")

#islower()
print("the output for islower function is", str1.islower())

print("\n")

#isupper()
print("the output for isupper function is", str1.isupper())

print("\n")

#isspace()
print("the output for isspace function is", str1.isspace())

print("\n")

#swapcase()
print("the output for swapcase function is", str1.swapcase())

print("\n")

#join()
n=int(input("enter no of strings"))
list1=[]
for i in range(n):
    list1.append(str1)
print("the strings is", list1)
j=input("enter the string for keeping the string in join function")
print("the output for join function is", j.join(list1))

print("\n")

#len()
print("the output for len function is", len(str1))

print("\n")

#lower()
print("the output for lower function is", str1.lower())

print("\n")

#upper()
print("the output for upper function is", str1.upper())

print("\n")

#index()
ind=input("enter the string to check the string index function")
print("the output for index function is", str1.index(ind))

print("\n")

#title()
print("the output for title function is", str1.title())

print("\n")

#isalpha()
print("the output for isalpha function is", str1.isalpha())

print("\n")

#isnumeric()
print("the output for isnumeric function is", str1.isnumeric())

print("\n")

