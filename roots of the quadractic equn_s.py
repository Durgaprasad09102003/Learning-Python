a = int( input("enter the coeff of x^2"))
b = int( input("enter the coeff of x"))
c = int( input("enter the coeff of constant"))
root1 = (-b +  (((b**2) - (4*a*c))**(1/2)))/2*a
root2 = (-b -  (((b**2) - (4*a*c))**(1/2)))/2*a
print("the roots are",root1,root2)