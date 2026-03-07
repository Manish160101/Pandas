'''

Similar to creating new column but no new column name

df["Column_name] = df["Column_name] and some operation or data

'''
import pandas as pd

Data = {

    "Name":["Manish","Aqdam","Sajal","Parveen"],
    "Age":[20,46,32,67],
    "Salary":[46000,24000,50000,32200]

}

df = pd.DataFrame(Data)

df["Salary"] = df["Salary"] * 1.05

print(df)