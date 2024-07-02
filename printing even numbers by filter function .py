def even(num):
        if num % 2 == 0:
            return True
list1 = list(map(int,input("enter the elements").split( )))
print(list1)

x = filter(even,list1)
print(list(x))