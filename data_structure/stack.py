# 3 PRACTICE PROBLEMS:
# P1 — reverse string using stack
# stack use karke string reverse karo
# "hello" → "olleh"
# (slicing [::-1] use mat karna! stack use karo!)

# stack = []
# for char in "hello":
#     stack.append(char)
# print(stack)


# append = []
# while len(stack) > 0:
#     append += stack.pop()
# print(append)

# P2 — valid brackets
# upar wala brackets example extend karo
# teen types handle karo: (), [], {}
# "({[]})"  → True
# "({[}])"  → False
# "((("     → False

# def is_valid(s):
#     stack = []
#     pair = {")":"(","}":"{","]":"["} # close-open mapping

#     for char in s:
#         if char in "({[":
#             stack.append(char)
#         elif char in ")}]":
#             if len(stack) == 0:
#                 return False
#             if stack.pop() != pair[char]:
#                 return False

#     return len(stack) == 0

# print(is_valid("({[]})"))
# print(is_valid("(("))


# input:
# visit("google.com")   → url string
# visit("youtube.com")  → url string
# visit("github.com")   → url string
# current()             → koi input nahi
# back()                → koi input nahi
# current()             → koi input nahi
# back()                → koi input nahi
# current()             → koi input nahi

# output:
# current() → github.com
# back()    → koi print nahi — bas pichle page pe jao
# current() → youtube.com
# back()    → koi print nahi
# current() → google.com


stack = []

def visit(url):
    stack.append(url)

def back():
    if len(stack) > 0:
        stack.pop()
    else:
        print("no more page")

def current():
    if len(stack) > 1:
        print(stack[-1])
    else:
        print("no more sites")

# use karo
visit("google.com")
visit("youtube.com")
visit("github.com")
current()   # github.com
back()
current()   # youtube.com
back()
current()   # google.com

    

    




