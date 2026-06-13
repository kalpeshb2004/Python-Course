# lst = ["hello", "ram", 10, 20, 30, 40, 50, 20]

# # print list
# print(lst)

# # first 3 elements
# print(lst[:3])

# # append
# lst.append("ram")
# print(lst)

# # extend
# lst.extend(["jay", "shree", "ram"])
# print(lst)

# # insert
# lst.insert(3, "hanuman")
# print(lst)

# # remove
# lst.remove(20)
# print(lst)

# # pop
# lst.pop(5)
# print(lst)

# # index
# print(lst.index("ram"))

# # count
# print(lst.count(20))

# # reverse
# lst.reverse()
# print(lst)

# # clear (keep this last)
# lst.clear()
# print(lst)

# P1 — list operations
# list lo [5,3,8,1,9,2,7]
# sort karo
# reverse karo
# max, min, sum print karo
# 8 ko remove karo

# lst = list(map(int,input("Enter a no: ").split()))
# print(lst)

# lst.sort()
# print(lst)

# #descending order me sort
# lst.sort(reverse=True)
# print(lst)

# lst.reverse()
# print(lst)

# print(sum(lst))

# print(max(lst))

# print(min(lst))

# lst.remove(8) #by value
# print(lst)

# lst.pop(2)
# print(lst)

# P2 — duplicate remover
# list lo [1,2,2,3,4,4,4,5]
# function banao jo duplicates hata de
# output → [1,2,3,4,5]

# def duplicates(lst):
#     lst1 = []
#     for x in lst:
#         if x not in lst1:
#             lst1.append(x)
#     return lst1
# lst = [1,2,2,3,4,4,4,5]
# print(duplicates(lst))

# P3 — student marks
# 5 students ke naam aur marks do alag lists me store karo
# highest marks wale ka naam print karo
# average nikalo
# pass (marks >= 40) aur fail alag print karo

# marks = [89,100,32,97,58]
# names = ["ram" , "sham" , "deven" , "alex" , "aanand"]

# ind_high_marks = marks.index(max(marks))
# for i in range(len(names)):
#     if ind_high_marks == i:
#         print(names[i])
#         break

# avg = sum(marks) / len(marks)
# print("evrage of Students: " , avg)

# for i in range(len(marks)):
#     if marks[i] >= 40:
#         print("pass")
#     else:
#         print("fail")
    







