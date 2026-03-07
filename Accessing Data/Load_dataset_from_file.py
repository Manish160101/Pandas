import pandas as pd

df = pd.read_excel("SampleSuperstore.xlsx")

pd.options.display.max_columns = 60

print(df.loc[[0,1]])