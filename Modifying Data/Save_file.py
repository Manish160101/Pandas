'''
We can save our data into files

'''
import pandas as pd

a = {
    "Name":['Manish','Aqdam','Sajal'],
    "Age":[20,40,23]
}

df = pd.DataFrame(a)

#print(df.to_csv("myData.csv", index=False)) #Convert data into csv file
#print(df.to_json("myData.json", index=False)) #Convert data into JSON file
#print(df.to_html("myData.html", index=False)) # converts data into HTML table