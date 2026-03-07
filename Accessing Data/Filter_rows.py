'''
we can filter rows using below methods.

loc["Index No"]
df[condition]
eg:- df[df["Salary"]==100000]

'''

import pandas as pd

data = {

    "Name":["Manish","Aqdam","Sajal","Parveen","Satish","Vicky","Amzad","Prabudha"],
    "Age":[20,25,26,34,23,42,32,39],
    "Salary":[50000,34200,23455,80000,127800,100000,340000,20000]
}

df = pd.DataFrame(data)

info = df[(df["Age"]>25) & (df["Salary"]>300000)]

print(info)


