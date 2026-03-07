'''
Selecting Columns 
two ways :
 - Series 
 - DataFrame

Column = df["Column_name"]
subset = df["Column1","Column2]

'''

import pandas as pd

data = {

    "Name":["Manish","Aqdam","Sajal","Parveen","Satish","Vicky","Amzad","Prabudha"],
    "Age":[20,25,26,34,23,42,32,39]
}

df = pd.DataFrame(data)
print(df["Name"])