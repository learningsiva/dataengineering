import pandas as pd

# extract part
# read the csv file from  local machine
print("extracting data from orders.csv")
data = pd.read_csv("orders.csv")
#print("raw data")
#print(data)

# transformation part
# converting sting to numeric data type(float) and null or empty values are replace with 0
data["amount"] = pd.to_numeric(data["amount"],errors='coerce').fillna(1)
# removing extra space before and after customer name
data["customer_name"] = data["customer_name"].str.strip()
print("after do transformations")
print(data)

# loading part
# save the clean data as csv file
data.to_csv("cleaned_orders.csv" , index=False)
#print("clean data is saved sucessfully")

