'''
We can fetch data from DataFrame using loc attribute.

loc[Index] => Gives output in series formate.
loc[[Index]] => if Index is passed as List, output comes in DataFrames.

'''

import pandas as pd

a = {
    "Name":['Manish','Aqdam','Sajal'],
    "Age":[23, 23, 21]
}

x = pd.DataFrame(a)

print(x.loc[1])   #Output format Series
print("==========")
print(x.loc[[0]]) # Output format DataFrame (Can be pass multiple indexes)
