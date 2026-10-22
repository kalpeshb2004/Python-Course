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
