# write a python program to print the fibonacci series:

#installing the list1, n, a and b in the program

n=int(input("enter the value of n"))
a=0
b=1

print("fibonacci series is ")
if n==1:
    print("\t",a)
elif n==2:
    print("\t",a)
    print("\t",b)
#using the loops upto the range n-1 we can add the numbers to the list1 by append():
else:
    print("\t",a)
    print("\t",b)
    for i in range(1,n-1):
        c=a+b
        a=b
        b=c
        print("\t",c)
        

    
    