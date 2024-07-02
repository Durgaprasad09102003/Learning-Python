# write a python program to print the string is palindrome or not:

#installing the x as string data type
x = str(input("enter the string"))
#reverse the string to form y:
y = x[::-1]
print("the reverse string is", y)

#if x and y equal then it is palindrome:
if x==y:
    print("given string is palindrome")
#else it is not a palindrome:
else:
    print("given string is not a palindrome")
    