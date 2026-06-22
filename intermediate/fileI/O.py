# P1 — Easy
# notes.txt file banao. User se 3 lines lo input se aur file me likho. Phir file padhke print karo.

# with open("notes.txt","w") as f:
#      for i in range(3):
#           enter = input(f"enter {i+1}: ")
#           f.write(enter + "\n")

# with open("notes.txt","r") as f:
#      content = f.read()

# print(content)


# P2 — Medium
# students.txt file me 5 students ka data likho (name, marks). File padho aur sirf passing students (marks >= 40) print karo.

# with open("students.txt" , "w") as f:
#     f.write("kalpesh,21\n")
#     f.write("jayesh,25\n")
#     f.write("ram,73\n")
#     f.write("krishna,78\n")
#     f.write("laxman,67")

# with open("students.txt","r") as f:
#     for line in f:
#         name,marks = line.strip().split(",")
#         marks = int(marks)
#         if marks >= 25:
#             print(name,marks)
