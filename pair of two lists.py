list1 = [1,3,5,7,9]
list2 = [2,4,6,8,0]
pair = [(x,y) for x in list1 for y in list2 if x!=y ]
print(pair)