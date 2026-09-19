1
# Two Sum — Array me do number dhundo jinka sum target ho, unke indices do.
# Input: [2,7,11,15], target=9 → Output: [0,1] ********

def two_sum(arr,target):
    seen = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            return [seen[complement] , i]
        seen[arr[i]] = i
    return []

print(two_sum([2,7,11,15],9))

2
# First non-repeating character — String me pehla aisa character dhundo jo sirf ek baar aaya ho.
# Input: "swiss" → Output: "w" **********

def non_repeate_char(str):
    freq = {}
    for ch in str:
        freq[ch] = freq.get(ch,0)+1
    for ch in str:
        if freq[ch] == 1:
            return ch
    return str

print(non_repeate_char("swiss"))

3
#saare non_reapeting char chaiye to result me collect karke return karo 
def non_repeate_char(str):
    freq = {}
    for ch in str:
        freq[ch] = freq.get(ch,0)+1

    result = []    
    for ch in str:
        if freq[ch] == 1:
            result.append(ch)
    return result

print(non_repeate_char("swiss"))

4
# Check anagram — Do string ke characters same frequency me hai kya check karo.
# Input: "listen","silent" → Output: True

def anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    freq = {}

    for ch in str1:
        freq[ch] = freq.get(ch,0) + 1
    for ch in str2:
        freq[ch] = freq.get(ch,0) - 1

    for count in freq.values():
        if count != 0:
            return False
    return True

print(anagram("listen" , "silent"))

5
# Find duplicates in array — Array me jo number ek se zyada baar aaye, unhe dhundo.
# Input: [1,2,3,2,4,1] → Output: [1,2]

def duplicates(arr):
    seen = set()
    result = []

    for x in arr:
        if x in seen and x not in result:
            result.append(x)
        seen.add(x)
    return result

print(duplicates([1,2,3,2,4,1]))

6
# Count frequency of each element — Har element kitni baar aaya, count karo.
# Input: [1,2,2,3,3,3] → Output: {1:1, 2:2, 3:3}

def freq(arr):
    freq = {}

    for x in arr:
        freq[x] = freq.get(x,0) + 1
    return freq

print(freq([1,2,2,3,3,3])) 

7
# . Check if array contains duplicate
# Input: [1,2,3,1] → Output: True

def check_duplicate(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False

print(check_duplicate([1,2,3,1,2]))

8
# **11. Find missing number (1 to N)**
# Input: `[1,2,4,5]`, N=5 → Output: `3`
# Approach: Agar 1 se N tak saare numbers hote, to unka sum ek formula se pata chal sakta hai: N*(N+1)/2. Actual array ka sum nikalo, expected sum se ghatao — jo bacha wahi missing number hai.

def missing_no(arr,n):
    axpected_sum = n * (n+1) // 2
    actual_sum = sum(arr)
    return axpected_sum - actual_sum

print(missing_no([1,2,4,5],5))

9
# **12. Intersection of two arrays**
# Input: `[1,2,2,1]`,`[2,2]` → Output: `[2]`

def intersection(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1 & set2)

print(intersection([1,2,2,1],[2,2]))

10
#  Ransom note check
# Input: ransom="aa", magazine="aab" → Output: True

def note_check(ransom,magazine):
    freq = {}
    for ch in magazine:
        freq[ch] = freq.get(ch ,0) + 1

    for ch in ransom:
        if freq.get(ch,0) <= 0:
            return False
        freq[ch] -= 1
    return True

print(note_check("aa" , "aab"))

11
# 25. Check if sentence is a pangram
# Input: "The quick brown fox jumps over the lazy dog" → Output: True

# Logic: Pangram = wo sentence jisme a-z ke saare 26 letters kam se kam ek baar aayein. 

# Sentence ko lowercase karo (case-insensitive check ke liye), har alphabet character (isalpha() — spaces/symbols skip) ko set me daalo (duplicates automatically avoid). Agar set ki final length 26 hai, matlab saare unique letters mil gaye → True.

def panagram(sentence):
    seen = set()

    for ch in sentence.lower():
        if ch.isalpha():
            seen.add(ch)
    return len(seen) == 26

print(panagram("The quick brown fox jumps over the lazy dog"))


12
#finding missing character to make two string anagram
# ex "abcd" "cbe" return: "d"

def miss_anagram(str1 ,str2):
    freq = {}

    for ch in str1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in str2:
        freq[ch] = freq.get(ch,0) - 1

    for ch , count in freq.items():
        if count != 0:
            return ch
    return None

print(miss_anagram("abcd" , "abc"))
























