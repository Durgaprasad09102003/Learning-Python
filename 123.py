def linearsearch(list1,key):
    for i in range(len(list1)):
        if key==list1[i]:
            print('element is found at the index:',i)
            break
    else:
        print('element is not found')
list1=[10,33,43,56,87,65]
print('original list is:',list1)
key=int(input('enter a key element is :'))
linearsearch(list1,key)