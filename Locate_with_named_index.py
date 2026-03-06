'''
we can also change name of index form 0 to n to some meaniful name
and same name can be used to fetch outputs.

'''

import pandas as pd

a = {
    "Name":['Manish','Aqdam','Sajal'],
    "Age":[23, 23, 21]
}

x = pd.DataFrame(a, index=['Student1','Student2','Student3'])

print(x)
print("======================================")
print(x.loc["Student1"])   #Output format Series
print("======================================")
print(x.loc[['Student2','Student3']]) # Output format DataFrame (Can be pass multiple indexes)
