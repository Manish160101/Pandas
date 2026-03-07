'''
A Pandas DataFrame is a 2 dimensional data structure, 
like a 2 dimensional array, or a table with rows and columns.

'''
import numpy as np
import pandas as pd

arr = np.array([["Manish","Sajal","Aqdam"],[20,23,12]])
#or
a = {
    "Name": ['Manish','Sajal','Aqdam'],
    "Age":[20,23,12]
}

#load data into a DataFrame object:
x = pd.DataFrame(arr)
y = pd.DataFrame(a, index=['a','b','c'])

print(y)
