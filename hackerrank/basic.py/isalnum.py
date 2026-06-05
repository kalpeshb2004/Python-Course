s = input()

alnum = False
alpha = False
digit = False
lower = False
upper = False

for char in s:
    if char.isalnum():
        alnum = True
    if char.isalpha():
        alpha = True
    if char.isdigit():
        digit = True
    if char.islower():
        lower = True
    if char.isupper():
        upper = True
        

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)


# s = input()

# alnum = False
# alpha = False
# digit = False
# lower = False
# upper = False

# for c in s:
#     if c.isalnum():
#         alnum = True
#     if c.isalpha():
#         alpha = True
#     if c.isdigit():
#         digit = True
#     if c.islower():
#         lower = True
#     if c.isupper():
#         upper = True

# print(alnum)
# print(alpha)
# print(digit)
# print(lower)
# print(upper)