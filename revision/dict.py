# DICT
# Q1 — Easy
# Student dict banao — name, marks (3 subjects). Average nikalo, highest subject batao.
student = {
    "name" : "kalpesh",
    "math" : 78,
    "science" : 96,
    "phy" : 76 
}

marks = []
for key,value in student.items():
    if key != "name":
        marks.append(value)

print(marks)
avg = sum(marks) / len(marks)
print(f'{avg:.2f}')

highest_sub = max(marks)
print(highest_sub)

# Q2 — Medium
# List of dicts lo (students) — marks ke basis pe filter karo (>=60), naam alphabetically sort karo.

# student = [{"name" : "kalpesh",
#             "marks" : 78},

#             {"name" : "jayesh",
#             "marks" : 10},

#             {"name" : "ram",
#             "marks" : 100}
#             ]

# filter = []
# for students in student:
#     if students["marks"] >= 60:
#         filter.append(students)
# print(filter)

# sort = sorted(student,key=lambda x: x["name"])
# print(sort)



