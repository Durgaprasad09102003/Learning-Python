# write a python program to print the prime numbers upto the interval p and q:

#installing the p and q values in the program:
p=int(input("enter the initial value"))
q=int(input("enter the final value"))

#the starting no is 2 to compare weather it is prime or not:
if p>1:
    print("the prime numbers between", p, "and", q, "is")
    #using loops we find the number is divisible by only itself:
    #other than that we call it as not a prime number:
    for i in range(p, q+1):
        Constant=False
        for j in range(2, q+1):
            if ((i%j==0) and (i!=j)):    
                Constant=True 
        if Constant==False:
            print(i)       
        