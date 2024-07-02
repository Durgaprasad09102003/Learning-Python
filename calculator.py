# write a python program to implement the simple arithmetic calculator

#defining the arithmetic operations
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
    
def calc():
    #installing  the inputs a and b
    a=int(input("enter the number:"))
    b=int(input("enter then number"))
    #for connecting to the operations
    op=int(input("MENU \n 1.add \n 2.sub \n 3.multi \n 4.div \n 5.mod \n select the operator"))
    if op==1:
        print("sum of a and b is",add(a,b))
    elif op==2:
        print("sub of a and b is",sub(a,b))
    elif op==3:
        print("multi of a and b is",multi(a,b))
    elif op==4:
        print("div of a and b is",div(a,b))
    elif op==5:
        print("mod of a and b is",mod(a,b))
 
calc()
 
 #to do again 
for i in range(11):
    a=input("do you want to do again? yes/no")
    if a=="yes":
        calc()
    else:
        break      