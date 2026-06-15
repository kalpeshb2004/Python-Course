# P1 — tuple operations
# tuple lo (5, 3, 8, 1, 9, 2, 7)
# max, min, sum print karo
# 8 kahan hai → index nikalo
# kitni baar 3 aaya → count karo
# list me convert karo → sort karo → wapas tuple banao

# tpl = (5, 3, 8, 1, 9, 2, 7)
# print(max(tpl))
# print(min(tpl))
# print(sum(tpl))
# print(tpl.index(8))
# print(tpl.count(3))
# lst = list(tpl)
# lst.sort()
# new_tpl = tuple(lst)
# print(new_tpl)

# 2 — student info
# 3 students ki info store karo tuple of tuples me:
# pythonstudents = (("ram", 20, 85), ("sam", 21, 90), ("tom", 19, 78))
# sabka naam print karo
# highest marks wala nikalo
# average age nikalo


# students = (("ram", 20, 85), 
#             ("sam", 21, 90), 
#             ("tom", 19, 78))

# print("Name: ")
# for names in students:
#     print(names[0])

# print("\nhighest Marks: ")
# high_marks = max(student[2] for student in students)
# print(high_marks)

# print("\nname of student who has highest marks: ")
# for student in students:
#     if high_marks == student[2]:
#         print(student[0])
    

# total_age = sum(student[1] for student in students)

# print("\navareage age of student: ")
# avarage_age = total_age / len(students[1])
# print(avarage_age)

# P3 — swap without temp
# 3 variables lo a=5, b=10, c=15
# tuple unpacking se swap karo:
# a=15, b=5, c=10

# a ,b ,c = 5 , 10 , 15

# a , b , c = c , a , b
# print(a , b , c)