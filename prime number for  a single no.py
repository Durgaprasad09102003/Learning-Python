# installation of a variable
X = int(input("enter a number:  "))
# to know a number is a prime the number should divisible by 1 and itself:
# we know that every number is divisible by 1

# to check the number is prime or not:
# we should check any other number is divisible or not with that number

number = False
if X == 2:
    number = False
for i in range(2, X):
    if X % i == 0:
        number = True
        break

if number:
    print(X, "is not a prime number")
else:
    print(X, "is a prime number")
