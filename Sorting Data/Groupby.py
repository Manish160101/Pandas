'''
Group by method is used to group some column on basis of some data

Syntax
df.groupby("column").aggregation_function()

Multilple aggregation:
df.groupby("Department")["Salary"].agg(["sum","mean","max"])

Common Aggregate Methods:
sum()
mean()
count() -> to count null values
min()
max()
std() -> Standard Deviation
Values_count() -> Used to sum of the occurence of each value
unique() -> To fin unique values in Column
'''

import pandas as pd

data = {
    "Name":["Manish","Aqdam","Sajal","Praveen","Satish"],
    "Age":[23,23,27,26,25],
    "Salary":[50000,34000,65000,54000,40000]
}


df = pd.DataFrame(data)

print(df.groupby(["Age"])["Salary"].agg(["sum","mean"]))
print(df["Age"].unique())
print(df["Age"].value_counts())