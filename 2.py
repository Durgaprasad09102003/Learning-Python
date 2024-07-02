def bubblesort(list):
    n = len(list)
    print("length of list is:", n)
    for i in range(n-1):
        for j in range(n-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                print(list)
            else:
                print(list)
        print()
    print('sorted list is:', list)
list1 = [14, 46, 43, 27, 57, 41, 45, 21, 70]
print('original list is:', list1)
bubblesort(list1)