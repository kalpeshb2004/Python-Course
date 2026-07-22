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

2
# P2 — Medium
# contacts.json — list of contacts. Program:

# Contact add karo → file update
# Name se search karo
# Contact delete karo → file update

# import json

# data = [
#     {"name": "Kalpesh", "phone": "9876543210"},
#     {"name": "Jayesh",  "phone": "8888888888"},
#     {"name": "Ram",     "phone": "9999999999"}
# ]

# with open("student1.json", "w") as f:
#     json.dump(data, f, indent=4)

# with open("student1.json", "r") as f:
#     data = json.load(f)

# data.append({"name": "kaya", "phone": "6777767777"})

# with open("student1.json", "w") as f:
#     json.dump(data, f, indent=4)

# # Search ✓
# for item in data:
#     if item["name"] == "kaya":
#         print(item["phone"], item["name"])

# # Delete ✓
# for contact in data:
#     if contact["name"] == "Kalpesh":
#         data.remove(contact)
#         break

# print(data)
