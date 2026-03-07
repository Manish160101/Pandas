'''
- Understanding the size of dataset
- Name of columns so later can be manipulated

Pandas provides shape and column attribute for this
df.shape -> It returns tuple of size -> (rows, columns)

'''

import pandas as pd

data = {

    "Name":["Manish","Aqdam","Sajal","Parveen","Satish","Vicky","Amzad","Prabudha"],
    "Age":[20,25,26,34,23,42,32,39]
}

df = pd.DataFrame(data)

print("================================")
print(df)
print("================================")
print(f"Shape: {df.shape}")
print(f"No of Rows: {df.shape[0]}")
print(f"No of Columns: {df.shape[1]}")
print(f"Name of Columns: {df.columns}")