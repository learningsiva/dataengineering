import pandas as pd

df  = pd.read_csv("customers-100.csv", index_col=0)

df["full_name"] = df["First Name"] + " " + df["Last Name"]
df  = df.drop(columns=["First Name", "Last Name"])
#print(df)

df.to_csv("cust.csv")