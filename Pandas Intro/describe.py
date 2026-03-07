'''
describe() -> This method is used to get statistical values of numerical columns in list

Output of below program:
             Age
count   8.000000    -> Columns without Null value
mean   30.125000    -> Avg of column
std     7.881941    -> Standard deviation(How far is values from Mean value of that data)
min    20.000000    -> Minimum value in Column
25%    24.500000    -> 1st quarter of Data
50%    29.000000    -> Median of data
75%    35.250000    -> 1st 3 quarters of Data
max    42.000000    -> Maximum value in data

'''
import pandas as pd

data = {

    "":["Manish","Aqdam","Sajal","Parveen","Satish","Vicky","Amzad","Prabudha"],
    "Age":[20,25,26,34,23,42,32,39]
}

df = pd.DataFrame(data)

print(df.describe())
