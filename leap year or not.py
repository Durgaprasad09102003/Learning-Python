# instalization of a variable
x = int(input("enter the year"))

#to check the given year is leap year we have to check the condition the a year should be divided by 4 the remainder should be equal to 0 and
#when the year is divided with 100 reminder should not be equal to 0

if (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
    print("given year is a leap year")
else:
    print("given year is not a leap year")
