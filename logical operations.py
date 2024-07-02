# logical operators

X = int(input("enter the value of x? "))

print("for and operator")

m = int(input("enter the m value? "))
n = int(input("enter the n value? "))

if X % m == 0 and X % n == 0:
    print("x is divided by both numbers")
else:
    print("x is not divided by one or both the number")

print("for or operator")

m = int(input("enter the m value? "))
n = int(input("enter the n value? "))

if X % m == 0 or X % n == 0:
    print("x is divided by one or both of the number")
else:
    print("x is not divided by both the numbers")
