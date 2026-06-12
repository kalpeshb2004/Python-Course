# enumerate → index + value suing list
# for loops (enumerate)
# lst = ["a" , "b" , "c"]
# for i , val in enumerate(lst):
#     print(i,val)

#two list together (zip)
# num = [111,222,333,444]
# str = ["aaa","bbb","ccc","ddd"]
# for n , s in zip(num,str):
#     print(n,s)

# 3 PRACTICE PROBLEMS:
# P1 — Multiplication table

# Take number from user. Print its table from 1 to 10.
# table = int(input("Enter num: "))
# for i in range(1,11):
#     print(table, "*" ,i, "=" ,table*i)

# P2 — Sum of digits
# Take number (e.g. 1234). Using loop, find sum of all digits.
# 1+2+3+4 = 10

# sum_no = int(input("enter a num: "))
# total = 0
# for i in range(len(str(sum_no))):
#     temp = sum_no % 10
#     total += temp
#     sum_no = sum_no // 10
# print(total)

# P3 — Pattern print
# Print this using nested loop:
# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end=" ")   
#     print()





