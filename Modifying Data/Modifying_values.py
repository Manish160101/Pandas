'''
We can modify any cell using loc method

.loc[row_index, "Column_name"] => Data
.loc[list_of_row_index,"Column_name"] => Changes value on all mentioned Index positions

'''
import pandas as pd

Data = {

    "Name":["Manish","Aqdam","Sajal","Parveen"],
    "Age":[20,46,32,67],
    "Salary":[46000,24000,50000,32200]

}

df = pd.DataFrame(Data)

df.loc[1,"Age"] = 24
print(df)

print("===============================")

df.loc[[1,3],"Age"] = 25

print(df)