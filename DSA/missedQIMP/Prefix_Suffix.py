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

# - palindrome one after removal (680): tumne kiya hai
# Input: "abca"
# Output: True
# (b ya c hata do to "aca" ya "aba" ban jaata)

def palindrome_one(str1):
    str1 = list(str1)
    left = 0
    right = len(str1) - 1

    while left < right:
        if str1[left] != str1[right]:
            temp = str1.copy()
            temp.pop(left)

            if temp == temp[::-1]:
                return True

            temp = str1.copy()
            temp.pop(right)

            if temp == temp[::-1]:
                return True
            return False

        left += 1
        right -= 1
    return True

print(palindrome_one("abca"))

# - Valid Palindrome II (680): tumne kiya hai, bas bina copy ke try karo
# 4. Valid palindrome (ignore spaces/punctuation, case)
# Input: "A man, a plan, a canal: Panama"

def valid_palindrome(sentence):
    left = 0
    right = len(sentence) - 1

    while left < right:
        while left < right and not sentence[left].isalnum():
            left += 1
        while left < right and not sentence[right].isalnum():
            right -= 1

        if sentence[left].lower() != sentence[right].lower():
            return False
        
        left += 1
        right -= 1

    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))

# Example 
# Input: [1, 0, 1, 0, 1, 0]
# Output: [0, 0, 0, 1, 1, 1]
    
def move_1s(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        while left < right and lst[left] != 1:
            left += 1
        while left < right and lst[right] != 0:
            right -= 1

        lst[left] , lst[right] = lst[right] , lst[left]
    return lst
print(move_1s([1, 0, 1, 0, 1, 0]))

# - Squares of sorted array: tumne kar liya hai
# Ek array diya hai jo sorted (ascending) hai, par usme negative numbers bhi ho sakte hain. Har number ka square nikalo aur result bhi sorted (ascending) order me return karo.

# Example 1
# Input: [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]

def sq_array(arr):
    left = 0
    right = len(arr) - 1
    result = []
    
    while left <= right:
        left_sqr = arr[left] ** 2
        right_sqr = arr[right] ** 2

        if left_sqr > right_sqr:
            result.append(left_sqr)
            left += 1
        else:
            result.append(right_sqr)
            right -= 1

    return result[::-1]

print(sq_array([-4, -1, 0, 3, 10]))


# day 3
# **4. Slow/Fast (easy)**

# - Find first and last occurrence using two pointers
# - Remove all occurrences of a value from string
# - Replace spaces in a string (in-place style)
# - Check if array is sorted

# Q: Find first and last occurrence using two pointers

# Ek array aur ek target diya hai. Array me target pehli baar kis index pe aaya aur aakhri baar kis index pe, dono batao. Do pointers se karna hai (ek shuru se, ek end se).

# Example 1
# Input: arr = [1, 2, 3, 2, 4, 2, 5], target = 2
# Output: (1, 5)
# (2 pehli baar index 1 pe, aakhri baar index 5 pe)

def first_last_occurence(arr,target):
    left = 0
    right = len(arr) - 1
    result = []

    while left < right:
        while left < right and arr[left] != target:
            left += 1
        while left < right and arr[right] != target:
            right -= 1

        result.append(left)
        result.append(right)
        break
    return result
print(first_last_occurence([1,2,3],9))

# Ek string aur ek character (value) diya hai. String me se us character ke saare occurrences hata do, baaki characters ka order same rakhna hai.

# Example 1
# Input: s = "programming", value = "r"
# Output: "pogamming"

def remove_char(str,value):
    str = list(str)
    slow = 0

    for fast in range(len(str)):
        if str[fast] != value:
            str[slow] = str[fast]
            slow += 1 

    return "".join(str[:slow])

print(remove_char("programming","r"))


# Q: Replace spaces in a string (in-place style)

# Ek string diya hai. Usme jahan bhi space hai, use %20 se badal do. Baaki characters ka order same rahe.

# Example 1
# Input: "my name is"
# Output: "my%20name%20is"

def replace_spaces(s, replace):
    result = []

    for ch in s:
        if ch == " ":
            result.append(replace)   # space ki jagah %20
        else:
            result.append(ch)        # baaki jaise the

    return "".join(result)

print(replace_spaces("my name is", "%20"))   # my%20name%20is

# Ek array diya hai. Check karo woh ascending (chhote se bade) order me sorted hai ya nahi. Sorted hai to True, warna False.

# Example 1
# Input: [1, 2, 3, 4, 5]
# Output: True

def sorted_array_check(arr):

    for fast in range(len(arr)-1):
        if arr[fast] > arr[fast + 1]:
            return False
    return True
    
print(sorted_array_check([1, 2, 3, 4, 5]))