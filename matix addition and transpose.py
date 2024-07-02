# write a python program to print the addition of two matrix and its transpose: 

#installing the function as fun:
def fun(X):
    #installing the x empty matrix:
    X=[[],[],[]]
    #using loops we add the elements in the matrix by append(): and return the matrix
    for i in range(0,3):
        for j in range(0,3):
            x=int(input())
            X[i].append(x)
        
    return X
   
        

#calling the function fun of arguments A and B
print("enter the values for matrix P")
P=fun("A")
print("the matrix P is")
for i in range(0,3):
    print(P[i])
print("enter the values for matrix Q")
Q=fun("B")
print("the matrix Q is")
for i in range(0,3):
    print(Q[i])


#adding the matrix to form C matrix:
C=[[], [], []]
for i in range(0,3):
    for j in range(0,3):
        C[i].append(P[i][j]+Q[i][j])
print("the sum of the matrix P and Q is")
for i in range(0,3):
    print(C[i])
    
#forming the transpose of the C matrix:
D=[[], [], []]
for i in range(0,3):
    for j in range(0,3):
        D[i].append(C[j][i])
print("the transpose of the matrix is")
for i in range(0,3):
    print(D[i])
