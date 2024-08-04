# Dictionary - Do not allow duplicate. Duplicate value will overwrite existing value

a = {"name": "Emc"}
print(a["name"])
b = {"name":"Siva",
     "City":"Trichy",
     "Age":39,
     "Family": ["Mohith","Latha","Muthiah","Prawin","Annam"]}
print(b["Family"])

#To print only the keys
print(b.keys())

#To print only values
print(b.values())

#We can modify values
b["Age"]=40
b.update({"City": "Bangalore"})
print(b.values())

# Delete values

b.pop("Age")
del b["City"]
print(b.values())

# To remove entire dictionary can use below
# del b