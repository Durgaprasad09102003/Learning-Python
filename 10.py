#write a python program to clean the data in the pandas dataframe

import pandas as pd
import numpy as np
dict1 = {"name": ["bunny", "nani", "ram"],
         "roll no": [10,11,12],
         "age": [25, 30, 28],}
df1 = pd.DataFrame(dict1)
print(df1)

df