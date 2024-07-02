n=int(input())
a=0
b=1
print(a,b)
while n>2:
    c=a+b
    print(c)
    a=b
    b=c
    n=n-1