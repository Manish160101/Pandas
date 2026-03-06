'''
We can pass Key/vaule pair as series.

In this Key of Dictionary becomes a Label instead of index

'''

import pandas as pd

calories = {
    "Sunday":20,
    "Monday":30,
    "Tuesday":50
}

x = pd.Series(calories)

print(x)