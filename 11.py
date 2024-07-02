# Write a Python program on Conditional operations on pandas dataframe
import pandas as pd

dict1 = {"name": ["bunny", "nani", "ram"],
         "age": [32, 30, 29],
         "income": [300000, 200000, 200000]}
df1 = pd.DataFrame(dict1)
print(df1)
df1["age = <=30"]= df1["age"].apply(lambda x: "true" if x <=30 else "false")
print(df1)

