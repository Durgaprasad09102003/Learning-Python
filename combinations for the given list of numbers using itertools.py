import itertools
print(dir(itertools))
set1 = set()
if 'combinations' in dir(itertools):
    from itertools import combinations
    A = list(map(int, input("enter the elements").split(" ")))
    print(A)
    for d in range(0, len(A)+1):
        temp = combinations(A, d)
        for i in list(temp):
            print(i)
            set1.add(i)

    print(set1)

