x = [1,2,3,4,5,6]
y =[]

for i in range(0,len(x),2):
    y = x[i:i+2]
    print(y,end=" ")

