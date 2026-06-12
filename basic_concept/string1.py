# P1 — vowel counter
# string lo, usme kitne vowels hai count karo
# "hello world" → 3

# str1 = "hbananio"
# count = 0
# for i in range(0,len(str(str1))):
#     temp = str1[i]
#     if str1[i] == "a":
#         count += 1
#     elif str1[i] == "e":
#         count += 1
#     elif str1[i] == "i":
#         count += 1
#     elif str1[i] == "o":
#         count += 1
#     elif str1[i] == "u":
#         count += 1
#     else:
#         pass
# print(count)

2 
# P2 — Caesar cipher
# har letter ko 3 position aage shift karo
# "abc" → "def"
# "xyz" → "abc" (wrap around!)

import string
alphabets = string.ascii_lowercase
# ab index nikalo aur shift karo!

print(alphabets.index("c"))
print(alphabets.index("z"))