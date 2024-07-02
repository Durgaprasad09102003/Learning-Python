punch = "!@#$%~`:;?.,|\_"
my = input("enter a string")
new = ""
for i in my:
    if i not in punch:
        new += i

print(new )