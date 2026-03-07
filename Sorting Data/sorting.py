'''
For sorting we can use sort_values() method

pass columnName or list of Columns to sort

sort_values(by = "Age", inplace = True, ascending=bool_value)

ascending = > True or False (False for descending)

if passing list in by = [] then pass [] in ascending as well

'''

import pandas as pd

data = {
    "Name":["Manish","Aqdam","Sajal","Praveen","Satish"],
    "Age":[23,23,27,26,25],
    "Salary":[50000,34000,65000,54000,40000]
}

df = pd.DataFrame(data)

print(df.sort_values(by = "Age",axis=0))  #sorting using single column
print(df.sort_values(by = ["Age","Salary"], axis=0, ascending=[False,True]))
