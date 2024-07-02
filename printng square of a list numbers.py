list1 = list(map(int, input(" enter the elements ").split(' ')))
print("original list is", list1)
l2 = []
def sq():
    for i in list1:
        i = i**2
        l2.append(i)
    print("final list is", l2)

sq()
