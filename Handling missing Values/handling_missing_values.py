'''
We can do following steps for this
 - remove rows or column containing Empty data
    This can be achieved by using dropna(axis=value,inplace=True) method
    axis = 0 -> Removes rows
    axis = 1 -> Removed Columns
 - Replace with some meaningful value
    This can be achieved by using fillna(value,inplace=True) method
'''
import pandas as pd

data = {

    "Name":["Manish","Aqdam","Sajal","Parveen"],
    "Age":[23,34,None,23],
    "Location":["Delhi","Pune","Chandigarh","Pune"]
}

df = pd.DataFrame(data)

print(df.dropna(axis=0))
print("===========================")
print(df.fillna({"Location":"Noida","Age":25},axis=0))

# we can also fill mean(), median() or mode() value

df["Age"].fillna(df["Age"].mean(), inplace=True)

print(df)
