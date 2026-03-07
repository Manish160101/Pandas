'''
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.

By Default labels(Index) is 0 to n 

we can modify index using index = value attribute.

'''

import pandas as pd

a = [4,6,7,2]

x = pd.Series(a)
y = pd.Series(a, index=['a','b','c','d'])

print(x)  #prints output with index 0 to n (Column1)
print(y)  #prints output with index a,b,c,d since we have specifiged as attribute. (This is called as Labels)
