'''
head(intvalue) -> It is used to fetch rows from top of dataset
tail(intvalue) -> It is used to fetch rows from last of dataset.

By default both gives 5 rows as ouput if no intvalue specified.

'''
import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print(df.head())
print("==========================================================")
print(df.tail())