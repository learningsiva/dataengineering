import pandas as pd

 # set 1 - extract the data
data1 = pd.read_csv("employees_dept1.csv")
data2 = pd.read_csv("employees_dept2.csv")



# combine the data
combine = pd.concat([data1, data2], ignore_index=True)


#set 2 - do transformations
# replace invalid values with 0 and convert into numbers
combine["salary"] = pd.to_numeric(combine["salary"], errors="coerce").fillna(0)
#print(combine)
# group by department and  sum salary
summary = combine.groupby("department")["salary"].sum().reset_index()
print(summary)

# load data
summary.to_csv("department_salary.csv", index=True)


