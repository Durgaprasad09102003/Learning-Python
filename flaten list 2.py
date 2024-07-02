x = [[1],[5,6,7],[8,9]]
print("original list",x)
y = []
for i in x:
    for j in i:
        y.append(j)
print('flatten list',y)
    