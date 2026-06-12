1
# #factorial of a number using recursion
# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(7)) 
# print(factorial(5))  

2
# #fibonicci series using recursion 
# def fibonicci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibonicci(n-1) + fibonicci(n-2)

3
# for i in range(10):
#     print(fibonicci(i), end=" ")    

# #sum_ of a number that returns a sum of num u to n num
# def sum1(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         return n + sum1(n-1)

# print(sum1(4))
# print(sum1(6))

4
# #power problem
# def power1(base,expo):
#     if expo == 0:
#         return 1
#     if expo == 1:
#         return base
#     else:
#         return base * power1(base,expo-1)
#     #ex:2**4 :  2   *      2**3

# print(power1(2,3))

5
#revesre string
# def rev_str(str):
#     if len(str) <= 1:
#         return str
#     else:
#         return str[-1] + rev_str(str[0:-1])

# print(rev_str("hello"))


6
# #counting char from a string
# def count1(str,sub_str):
#     if str == "":
#         return 0
    
#     if str[0] == sub_str:
#         return 1 + count1(str[1:] ,sub_str)
#     else:
#         return 0 + count1(str[1:] ,sub_str)
# print(count1("hello","l"))
               