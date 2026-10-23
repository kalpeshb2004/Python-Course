# 1. Common Prefix (exam wala pattern, pehle ye karo)

# Common prefix of 2 strings: "flower", "flow" → "flow"
# Common suffix of 2 strings: "testing", "running" → "ing"
# Longest Common Prefix (14): list of strings, ["flower","flow","flight"] → "fl"
# Counting Words With a Given Prefix (2185)
# Check If a Word Occurs As a Prefix of Any Word in a Sentence (1455)

# Common prefix of 2 strings: "flower", "flow" → "flow"
def common_prefix(str1,str2,str3):
    i = 0 

    while i < len(str1) and i < len(str2) and i < len(str3):
        if str1[i] == str2[i] == str3[i]:
           i += 1
        else:
            break  
    return str1[:i]

print(common_prefix("flower","floing","flower"))

# Common suffix of 2 strings: "testing", "running" → "ing"
def common_suffix(str1,str2,str3):
    str1 = str1[::-1]
    str2 = str2[::-1]
    str3 = str3[::-1]
    i = 0
    result = ""
   
    while i < len(str1) and i < len(str2) and i < len(str3):
        if str1[i] == str2[i] == str3[i]:
            result += str1[i]
            i += 1  
        else:
            break
    return result[::-1]

print(common_suffix("testing","rinning","ing"))

# Longest Common Prefix (14): list of strings, ["flower","flow","flight"] → "fl"

def common_prefixx(str1,str2,str3):
    i = 0

    while i < len(str1) and i < len(str2) and i < len(str3):
        if str1[i] == str2[i] == str3[i]:
            i += 1
        else:
            break
    return str1[:i]
print(common_prefixx("flower","flow","flight"))

# Counting Words With a Given Prefix (2185)
# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# (attention aur attend “at” se shuru hote hain)

def match_prefix(words , pref):
    count = 0
    n = len(pref)
    for word in words:
      if word[:n] == pref:
          count += 1      
    return count

print(match_prefix(["pay","attention","practice","attend"],"at"))

# Example 1
# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# (“burg”, 4th word burger ka prefix hai)

def searchWord_prefix(sentence,searchWord):
    sentence = sentence.split(" ")
    n = len(searchWord)

    for i, word in enumerate(sentence):
        if word[:n] == searchWord:
            return i+1
    return []
print(searchWord_prefix("i love eating burger","burg"))


# **2. Do strings pe parallel pointers**

# - Is Subsequence (392): tumne kar liya hai
# - Merge Strings Alternately (1768): `"abc"`, `"pqr"` → `"apbqcr"`
# - Count matching characters at same index of two strings
# - Check if two strings are equal after ignoring spaces (do pointers se)

# day 2 
# example 6
# - Merge Strings Alternately (1768): `"abc"`, `"pqr"` → `"apbqcr"`

def alternate_string(str1,str2):
    i = 0
    result = ""

    while i < len(str1) and i < len(str2):
        result += str1[i]
        result += str2[i]
        i += 1

    result += str1[i:]
    result += str2[i:]

    return result

print(alternate_string("abc","pqr"))

# Do strings s aur t hain. Check karo s, t ka subsequence hai kya.
# Example 7
# Input: s = "abc", t = "ahbgdc"
# Output: True

def is_subsequence(s,t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)

print(is_subsequence("abc","ahbgdc"))

# Do strings diye hain. Dono me same position pe kitne characters barabar hain, woh count karo.

# Example 8
# Input: str1 = "hello", str2 = "hallo"
# Output: 4
# (position 0: h=h, 1: e≠a, 2: l=l, 3: l=l, 4: o=o, to 4 match)

def count_match(str1,str2):
    i = 0
    count = 0
    while i < len(str1) and i < len(str2):
        if str1[i] == str2[i]:
            count += 1
        i += 1
    return count
print(count_match("hello","hallo"))
            
# Do strings diye hain. Spaces hata dene ke baad dono barabar hain kya, check karo. Yeh do pointers se karna hai, replace() ya naya string banaye bina.

# Example 9
# Input: str1 = "he llo", str2 = "hel lo"
# Output: True
# (spaces hatane par dono "hello")

def spaces_ignore_match(str1,str2):
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        while i < len(str1) and not str1[i].isalnum():
            i += 1
        while j < len(str2) and not str2[j].isalnum():
            j += 1

        if str1[i] != str2[j]:
            return False

        i += 1
        j += 1
        
    return True
print(spaces_ignore_match("he llo","hel lo"))

# day 2 same day
# **3. Opposite-end (easy)**

# - Valid Palindrome II (680): tumne kiya hai, bas bina copy ke try karo
# - Move all 1s to right in binary array
# - Sort 0s and 1s (binary array sort)
# - Sort Colors (75): 0, 1, 2 (thoda medium, last me karna)
# - Squares of sorted array: tumne kar liya hai

