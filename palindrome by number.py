#write a python program to check the palindrome for a number

# #installing the input n
n=int(input("enter a number"))
temp=n
rev=0
#by using while loop we can reverse the number
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
#checking the palindrome
if(temp==rev):
    print(temp," is palindrome")
else:
    print(temp,"is not a palindrome")
