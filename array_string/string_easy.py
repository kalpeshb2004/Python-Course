# # reverse a string
# word = 'kalpesh'
# print(word[::-1])

# reverse = ""
# for w in word:
#     reverse = w + reverse

# print(reverse)

# string palindrom
# word = 'nayak'
# rev = ''

# for w in word:
#     rev = w + rev

# if rev == word:
#     print("palindrom")
# else:
#     print("not")

# counting vowels and consonent
# word = 'kalpesh'
# consonent = 0
# vowels = 0
# for w in word:
#     if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
#         vowels += 1
#     else:
#         consonent += 1

# print(vowels)
# print(consonent)

# Count the frequency of each character
# freq = {}
# word = 'kalpeshphsk'

# for w in word:
#     if w in freq:
#         freq[w] += 1
#     else:
#         freq[w] = 1

# for w in freq:
#     print(w,freq[w],end="")

# Find the length of a string without using len()
# word = 'kalpesh'
# count = 0
# for w in word:
#     count +=1
# print(count)

# # Check if two strings are equal without using ==
# word = 'kalpesh'
# word1 = 'aalpesh'

# if word == word1:
#     print("equal")
# else:
#     print("not equal")

# Remove all whitespace from a string
# word = 'kalpesh bhure hello'
# result =""
# for ch in word:
#     if ch != " ":
#         result += ch

# print(result)

# Count the number of words in a sentence
# word = 'kalpesh bhure hello'
# print(len(word.split()))

# Find the first non-repeating character
# freq = {}
# word = 'kkzbkaapdegsjajkew'

# for w in word:
#     if w in freq:
#         freq[w] += 1
#     else:
#         freq[w] = 1

# for w in freq:
#     if freq[w] == 1:
#         print(w)
#         break

word = 'kkzbkaapdegsjajkew'
index = word.rfind("a")
print(index)





    
    
    
        






