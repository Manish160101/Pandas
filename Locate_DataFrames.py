'''
We can fetch data from DataFrame using loc attribute.

loc[Index] => Gives output in series formate.
loc[[Index]] => if Index is passed as List, output comes in DataFrames.

we can also change name of index form 0 to n to some meaniful name

'''

import pandas as pd

a = {
    "Name":['Manish','Aqdam','Sajal'],
    "Age":[23, 23, 21]
}

x = pd.DataFrame(a, index=['Student1','Student2','Student3'])

#print(x.loc[1])   #Output format Series
#print("==========")
#print(x.loc[[0]]) # Output format DataFrame (Can be pass multiple indexes)
print(x)
