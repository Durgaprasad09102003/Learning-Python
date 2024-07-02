lower = 10
upper = 20
print("prime numbers between ", lower, "and", upper, "are")
for num in range(lower,upper+1):
    sum =0
    for i in range (1, num+1):
        if (num%1) == 0:
            sum = sum +1
        if sum == 2:
            print(num, end=" ")