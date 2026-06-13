#sqaure if no is even and cube if the no is odd
# lst = [n**2 if n%2==0 else n**3 for n in range(1,10)]
# print(lst)

# P1 — filter + transform
# list lo [1,2,3,4,5,6,7,8,9,10]
# comprehension se new list banao jisme:
# sirf odd numbers ho
# aur unka cube ho
# output → [1, 27, 125, 343, 729]

# lst = [1,2,3,4,5,6,7,8,9,10]
# lst1 = [i**3 for i in lst if i%2 != 0]
# print(lst1)

# P2 — string filter
# list lo ["apple","bat","cat","elephant","dog","ant"]
# comprehension se sirf wo words nikalo:
# jinka pehla letter a ho
# output → ["apple","ant"]

# lsts = ["apple","bat","cat","elephant","dog","ant"]

# lst1 = [i for i in lsts if i[0] == "a"]
# print(lst1)

# P3 — FizzBuzz list
# 1 se 20 tak list banao jisme:
# number 3 se divide ho → "Fizz"
# number 5 se divide ho → "Buzz"
# dono se ho → "FizzBuzz"
# kuch nahi → number hi rakho
# output → [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, ...]

# lst = ["Fizz" if i%3==0 else("Buzz" if i%5==0 else("FizzBuss" if i%3==0 and i%5==0 else i)) for i in range(1,20)]
# print(lst)

