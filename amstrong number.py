 # instalization of a variable
num1 = int(input("enter the number"))
y = len(str(num1))
z = int(y)
print("number of digits are", z)
SUM = 0
num2 = num1
while num2 > 0:
    digit = num2 % 10
    SUM += digit ** z
    num2 //= 10

print("sum is ", SUM)
if num1 == SUM:
    print("given number is amstrong number")
else:
    print("given number is not a amstrong number")
