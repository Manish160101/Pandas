'''
To know about Data.
No of Columns, rows or what type of Data which rows is containing we have method in pandas called:
info()

'''
import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print(df.info())