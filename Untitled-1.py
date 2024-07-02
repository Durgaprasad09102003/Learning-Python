def findNthNumber(A, B, N):
    sum = 0
    for i in range(2, N):
        sum = A + B
        A = B
        B = sum
    return sum
 
n=int(input())
for i in range(0,2):
    print(findNthNumber(2,3,4))