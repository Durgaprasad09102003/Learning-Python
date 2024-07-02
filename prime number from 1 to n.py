num = int(input("enter a number"))
constant = False
for i in range(2, num + 1):
    for j in range(2, i+1):
        if i % j == 0 and i != j:
            constant = True
            break
        else:
            constant = False
    if constant == True:
        print(i, "is not a prime number")
    else:
        print(i, "is a prime number")
