import numpy as np
print(dir(np))
list1=[[3,6,9],[12,np.nan,8],[21,25,np.nan]]
print("given list is",list1)
array1=np.array(list1)
print("input array is",array1)
print("rows with numerical data")
print(np.isnan(array1).any(axis=1))
