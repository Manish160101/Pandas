'''

Missing values can be of different types

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates

isnull() method used to detect null values in dataset.
It returns boolean values

'''

import pandas as pd

data = {

    "Name":["Manish","Aqdam","Sajal","Parveen"],
    "Age":[23,34,None,23],
    "Location":["Delhi",None,"Chandigarh","Pune"]
}

df = pd.DataFrame(data)

print(df.isnull())
print(df.isnull().sum())