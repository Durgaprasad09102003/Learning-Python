x = [[], [], []]
L = [[], [], []]
for i in range(0, 3):
    for j in range(0,3):
        y = int(input("enter the values for the list x:"))
        x[i].append(y)
print(x)
for i in range(0, 3):
    for j in range(0,3):
        L[i].append(x[j][i])
print(L)
