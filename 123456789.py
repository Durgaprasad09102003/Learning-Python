def add1(name,roll,*num):
    print('student-',name)
    print('roll-',roll)
    sum = 0
    for i in num:
        sum = sum+i
    print('SUM = ', sum)


a = input("enter a name")
b = int(input("enter roll no"))
add1(a, b, 1, 52, 3, 65)