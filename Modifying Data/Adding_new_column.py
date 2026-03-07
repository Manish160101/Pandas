'''
We have two ways to Iclude new Columns using Pandas

- Square Brackets
df["Column_name"] = Some_data  # This will create new Column with mentioned Name

- Insert method
df.insert(loc, "Column_name", some_data) -> loc should be index value where u want to insert new Column

'''

import pandas as pd

Data = {

    "Name":["Manish","Aqdam","Sajal","Parveen"],
    "Age":[20,46,32,67],
    "Salary":[46000,24000,50000,32200]

}

df = pd.DataFrame(Data)

df["Location"] = ["Gurugram","Pune","Noida","Delhi"]   #using Square bracket

df.insert(0,"Emp_id",[20,21,22,23])  #using Insert method

print(df)