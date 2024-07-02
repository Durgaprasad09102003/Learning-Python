# write a python program to print the factorial of the given number:

#installing the x, i and fact in the program
x = int(input("enter the number"))
i = 1
fact=1

#using loops we can find factorial of the given number x:
while i<=x:
    fact *= i
    i += 1
#printing the factorial of the given number
print("the factorial of the given number is",fact)