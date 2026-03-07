'''
Method called interpolate calculates estimate value by checking other values of that column

interpolate(method=,axis=value,inplace=True)
method => linear, polynomial, time etc.

If first value is missing interpolation without limit will not work as it needs prev and next value
to calculate estimate.

Syntax: df.interpolate(method="linear", limit_direction="both")  
where limit_direction can be both, forward, backward

==========================

How Interpolation works:

30 -> None -> 40 => 40 - 30 = 10
Index diff -> 4-2 => 2
step size => 10/2 -> 5
estimate value => 30 + 5 => 35


Use cases:
1 - For time series data
2 - Numeric data with trends
3 - Avoid dropping rows
4 - 

'''
import pandas as pd

data = {
    "Name":["Manish","Aqdam","Sajal","parveen","Anshul"],
    "Age":[10,20,30,None,50]
}

df = pd.DataFrame(data)

df["Age"] = df["Age"].interpolate(method="linear", axis=0).astype(int)

print(df)

