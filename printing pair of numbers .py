x = []
n = int(input("enter the no of elements"))
for i in range(0, n):
    y = int(input("enter the elements"))
    x.append(y)
print(x)

x.sort()
print(x)
l1 = []
l2 = []
if n % 2 == 0:
    b = n // 2
    for i in range(0, b):
        l1.append(x[i])
    for j in range(b, n):
        l2.append(x[j])
    print(l1)
    print(l2)


if n % 2 != 0:
    b = n//2
    for i in range(0, b+1):
        l1.append(x[i])
    for j in range(b, n):
        l2.append(x[j])
    print(l1)
    print(l2)

l3 = []
l2.reverse()
l3.append(l2)
print(l3)
print(list(zip(l2, l1)))
