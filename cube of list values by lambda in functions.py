print("enter the values")
y = list(map(int, input().split()))
print("original list is", y)

cube = []
for i in range(len(y)):
    X = lambda a: a**3
    cube.append(X(y[i]))

print(" cube of original list ", cube)
