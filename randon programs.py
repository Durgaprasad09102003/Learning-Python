import random
print(random.random())
print(random.uniform(0, 5))
print(random.randint(0, 5))
print(random.getrandbits(5))
seq = list(map(int,input("enter the values").split(",")))
print(seq)
print(random.choice(seq))