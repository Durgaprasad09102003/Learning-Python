n = int(input("enter the no of elements"))
x = []
for i in range(0, n):
    y = int(input("enter the elements"))
    x.append(y)
print(x)

p = [num for num in x if num % 2 == 0]
print(p)
