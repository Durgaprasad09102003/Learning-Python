# Python program for implementation of Selection Sort

A = list(map(int, input("enter the elements \n").split(",")))
print(A)
# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    minimum = i
    for j in range(i + 1, len(A)):
        if A[minimum] > A[j]:
            minimum = j

    # Swap the found minimum element with
    # the first element
    A[i], A[minimum] = A[minimum], A[i]

# Driver code to test above
print("Sorted array")
for i in range(len(A)):
    print((A[i]))
