# P1 — Easy
# Phone book banao. 3 contacts store karo (name→number). User se naam lo, number print karo. Naam nahi mila toh "Contact not found" print karo.

# book = {
#     "name" : ["kalpesh","jayesh","ram"],
#     "number" : [9420353913,8383864558,1234567890]
# }

# search = input("enter a number: ")

# if search in book["name"]:
#     index = book["name"].index(search)
#     print("numbers: " , book["number"][index])
# else:
#     print("users not found")

# # Simple direct dict — naam → number
# book = {
#     "kalpesh": 9420353913,
#     "jayesh": 8383864558,
#     "ram": 1234567890
# }

# search = input("Enter name: ")

# if search in book:
#     print("Number:", book[search])  # direct access, no index needed
# else:
#     print("Contact not found")



# P2 — Medium

# List of words lo. Har word kitni baar aaya count karo using dict.
# Input:  ["apple", "mango", "apple", "banana", "mango", "apple"]
# Output: {"apple": 3, "mango": 2, "banana": 1}

# lsts = ["apple", "mango", "apple", "banana", "mango", "apple"] 

# count_apple = 0
# count_mango = 0
# count_banana = 0

# for lst in lsts:
#     if lst == "apple":
#         count_apple += 1
#     elif lst == "mango":
#         count_mango += 1
#     elif lst == "banana":
#         count_banana += 1
# dict = {"apple" : count_apple ,
#         "mango" : count_mango,
#         "banana" : count_banana}
# print(dict)

# 2nd best apporach

# lsts = ["apple", "mango", "apple", "banana", "mango", "apple"]

# count = {}

# for lst in lsts:
#     if lst in count:
#         count[lst] += 1
#     else:
#         count[lst] = 1
# print(count)


# P3 — Hard
# Student marks dict banao (3 subjects). Program karo jo:
# Average nikale
# Highest subject bataye
# Pass/Fail decide kare (passing = 40 per subject)

marks = {
    "maths": 85,
    "science": 92,
    "english": 78
}

sum_marks = sum(marks.values())
print("total marks : ",sum_marks)

avg_marks = sum_marks / len(marks.values())
print("avrage mark: " ,avg_marks)

max_marks = max(marks.values()) 
print("highest marks: ",max_marks)

for subjects , marks in marks.items():
    if marks >= 40:
        print(subjects , "pass")
    else:
        print(subjects ,"failed")




        

