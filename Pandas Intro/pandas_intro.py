'''
Pandas is a python library used for data manipulation and data analysis.

Key features:
- Works seamlessely with Structured data formats like csv.
- Handles missing values easily.
- Built on Numpy for fast computation

'''
import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print(df)