# P1 — Easy
# student.json banao — name, age, marks (3 subjects list). File me save karo, load karo aur sab print karo. Average bhi nikalo marks list se.

import json

student = {
    "name" : "kalpesh",
    "age" : "21",
    "marks" : [87,67,72]
}

#save
with open("student.csv","w") as f:
    json.dump(student,f,indent=4)

#laod
with open("student.csv","r") as f:
    data = json.load(f)

#print
print(data["name"])
print(data["age"])
print(data["marks"])

#average
average = sum(data["marks"]) / len(data["marks"])
print(f"{average:.2f}")

