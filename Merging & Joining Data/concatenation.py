'''
concatenation is used to merge two datarames either horizontally or vertically

pd.concat()
Syntax:
pd.concat(objs, axis=0, join="outer", ignore_index=False)

objs	-> list of DataFrames
axis	-> 0 → rows, 1 → columns
join	-> outer or inner
ignore_index ->	reset index

Use case:
Combining Monthly sales report

df1 → January sales
df2 → February sales
df3 → March sales

pd.concat([df1, df2, df3], axis=value)

'''

import pandas as pd

df1 = pd.DataFrame({
    "Name":["Manish","Aqdam"],
    "Age":[25,30]
})

df2 = pd.DataFrame({
    "Name":["Sajal","Anshul"],
    "Age":[28,35]
})

df_concat = pd.concat([df1,df2], ignore_index=True)
print(df_concat)
df_concat1 = pd.concat([df1,df2], axis=1, ignore_index=True)
print(df_concat1)