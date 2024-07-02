print("On")

select = ('+', '-', '*', '/', '=')


def add(x):
    y = int(input())
    t = x + y
    return t

def sub(x):
    y = int(input())
    t = x - y
    return t

def multi(x):
    y = int(input())
    t = x * y
    return t

def div(x):
    y = int(input())
    t = x / y
    return t


x = int(input())

for i in range(1, 11, 1):
    A=str(input("enter the operator"))

    if A in select:
        if A == '+':
            x = add(x)
        elif A == '-':
            x = sub(x)
        elif A == '*':
            x = multi(x)
        elif A == '/':
            x = div(x)
        elif A == '=':
            break
    else:
        print("'invalid' try other arithmetic operator")
print(x)
