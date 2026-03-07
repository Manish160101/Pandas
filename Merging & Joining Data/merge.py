'''
syntax:
df.merge(df1,df2, on="Column_name", how="type_of_join")

'''
import pandas as pd

df_cutomer = pd.DataFrame({
    "Customer_ID":[1,2,3],
    "Name":["Manish","Parveen","Aqdam"]
})

df_orders = pd.DataFrame({
    "Customer_ID":[1,2,4],
    "Order_ID":[23,54,21]
})

print(df_cutomer)
print(df_orders)

df_merged = pd.merge(df_cutomer,df_orders,on="Customer_ID",how="inner") # only prints matching values(means data present in both columns)
print(df_merged)
df_merged1 = pd.merge(df_cutomer,df_orders,on="Customer_ID",how="outer") # prints all values of both table and fills NaN for not available data
print(df_merged1)
df_merged2 = pd.merge(df_cutomer,df_orders,on="Customer_ID",how="left") #keeps all values from left table and gives Nan if value not present in right table
print(df_merged2)
df_merged3 = pd.merge(df_cutomer,df_orders,on="Customer_ID",how="right") # vice versa of above, print all values of right table
print(df_merged3)