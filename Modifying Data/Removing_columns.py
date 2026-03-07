'''
It helps in keeping Data clean

Pandas provides drop() method
Syntax:
df.drop(columns = ["ColumnName"])  creates new data
or 
df.drop(columns = ["ColumnName"], inplace = True)  #To modify original dataFrame
or pass list of Columns to remove multiple columns

'''
import pandas as pd

Data = {

    "Name":["Manish","Aqdam","Sajal","Parveen"],
    "Age":[20,46,32,67],
    "Salary":[46000,24000,50000,32200]
}

df = pd.DataFrame(Data)

print(df.drop(columns="Age")) # or use inplace=True

