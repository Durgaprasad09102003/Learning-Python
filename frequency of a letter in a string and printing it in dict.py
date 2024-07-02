x = input("enter a string")
y = {}
for i in x:
    count = 0
    for j in x:
        if i == j:
            count += 1
    y[i] = count
print(y)
