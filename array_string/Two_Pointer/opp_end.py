# Two pointer
1
# Reverse a string
# Input: "hello"
# Expected Output: "olleh"

# def reverse(s):
#     s = list(s)
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         s[left] , s[right] = s[right] , s[left]
#         left += 1
#         right -= 1

#     return "".join(s)

# print(reverse("hello"))

2
# 2. Reverse an array
# Input: [1, 2, 3, 4, 5]
# Expected Output: [5, 4, 3, 2, 1]

# def array(arr):
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         arr[left] , arr[right] = arr[right] , arr[left]
#         left += 1
#         right -= 1

#     return arr

# print(array([1,2,3,4,5]))

# # 3. Check palindrome (string)
# # Input: "madam"
# # Expected Output: True
# # Input 2: "hello"
# # Expected Output: False

# def  palindrome(s):
#     s = list(s)
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# print(palindrome("madam"))

# 4. Valid palindrome (ignore spaces/punctuation, case)
# Input: "A man, a plan, a canal: Panama"
# Expected Output: True
# Input 2: "race a car"
# Expected Output: False

# def valid_palindrome(s):
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         while left < right and not s[left].isalnum():
#             left += 1
#         while left < right and not s[right].isalnum():
#             right -= 1

#         if s[left].lower() != s[right].lower():
#             return False

#         left += 1
#         right -= 1

#     return True

# print(valid_palindrome("A man, a plan, a canal: Panama"))

# 5. Pair with given sum (sorted array)
# Input: arr = [1, 2, 3, 4, 6], target = 6
# Expected Output: (1, 3) (index) ya (2, 4) (values) — pair jinka sum 6 ho     

# arr = [1,2,3,4,6]
# target = 6

# left = 0
# right = len(arr) - 1

# while left < right:
#     total = arr[left] + arr[right]

#     if total == target:
#         print(arr[left] , arr[right])
#         break
#     elif total < target:
#         left += 1
#     elif total > target:
#         right -= 1
    
# 6. Reverse vowels of a string
# Input: "hello"
# Expected Output: "holle"
# Input 2: "leetcode"
# Expected Output: "leotcede" 

# def vowels_swpping(s):
#     s = list(s)
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         while left < right and s[left] not in "aeiou":
#             left += 1
#         while left < right and s[right] not in "aeiou":
#             right -= 1

#         s[left] , s[right] = s[right] , s[left]

#         left += 1
#         right -= 1

#     return "".join(s)

# print(vowels_swpping("hello"))
# print(vowels_swpping("leetcode"))

# 7. Check if string is palindrome after removing at most 1 character
# Input: "abca"
# Expected Output: True (b ya c hatao to "aca" ya "aba" palindrome ban jaata)
# Input 2: "abc"
# Expected Output: False

# def palindrome(s):
#     s = list(s)
#     left = 0
#     right = len(s) - 1

#     while left < right:
#        if s[left] != s[right]:
#            temp = s.copy()
#            temp.pop(left)

#            if temp == temp[::-1]:
#               return True

#            temp = s.copy()
#            temp.pop(right)

#            if temp == temp[::-1]:
#                return True

#            return False
#        left += 1
#        right -= 1

#     return True

# print(palindrome("abca"))

# 8. Reverse a string maintaining word order *******
# Input: "I love Java"
# Output: "I evol avaJ"
# (Har word ke letters reverse, but word order same)

# def reverse_maintain_order(s):
#     words = s.split(" ")
#     result = []

#     for word in words:
#         word = list(word)
#         left = 0
#         right = len(word) - 1

#         while left < right:
#             word[left] , word[right] = word[right] , word[left]
#             left += 1
#             right -= 1

#         result.append("".join(word))

#     return " ".join(result)

# print(reverse_maintain_order("I Love Java"))

# 9. Compare Version Numbers
# Input: version1 = "1.2", version2 = "1.10"
# Output: -1
# Input 2: version1 = "1.01", version2 = "1.001"
# Output: 0

# def compare_version(version1,version2):
#     parts1 = version1.split(".")
#     parts2 = version2.split(".")

#     max_len = max(len(parts1), len(parts2))

#     i = 0

#     while i < max_len:
#         num1 = int(parts1[i]) if i < len(parts1) else 0
#         num2 = int(parts2[i]) if i < len(parts2) else 0

#         if num1 < num2:
#             return -1
#         if num1 > num2:
#             return 1

#         i += 1

#     return 0

# print(compare_version("1.2", "1.10"))     # -1
# print(compare_version("1.01", "1.001"))

# 10
# left side even and right side all odd (no need to maintain order)
# sort array by parrity

def parity(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while left < right and arr[left] % 2 == 0:
            left += 1

        while left < right and arr[right] % 2 != 0:
            right -= 1

        arr[left] , arr[right] = arr[right] , arr[left]
        left += 1
        right -= 1

    return arr

print(parity([3,1,2,4]))


# 11. Two Sum II (sorted array, indices)
# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]

def two_sum_index(arr):
    left = 0
    right = len(arr) - 1
    target = 9

    while left < right :
        total = arr[left] + arr[right]
        if total == target:
            return [left+1 , right+1]
        elif total < target:
            left += 1
        elif total > target:
            right -= 1      
    return -1

print(two_sum_index([2, 7, 11, 15]))

# Q12
# Reverse Only Letters
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

def rev_only_ltter(s):
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        s[left] , s[right] = s[right] , s[left]
        left += 1
        right -= 1

    return "".join(s)

print(rev_only_ltter("a-bC-dEf-ghIj"))


# 13. Palindrome After One Swap
# Input: [1, 2, 4, 2, 1]
# Output: True

def palindrome_one_after_swap(arr):
    left, right = 0, len(arr) - 1

    # jab tak match ho, dono pointer andar aao
    while left < right and arr[left] == arr[right]:
        left += 1
        right -= 1

    if left >= right:
        return True   # already palindrome, swap ki zarurat nahi

    # ek hi mismatch pair par swap try karo
    arr[left], arr[right] = arr[right], arr[left]
    return arr == arr[::-1]

print(palindrome_one_after_swap([1, 2, 4, 2, 1]))  # True

# Q 14. Minimum Length After Removing Similar Ends
# Input: "cabaabac"
# Output: 0
# explain : opp/end same he to  remove karo 0 hone tak / jaha same na mile loop break karo aur utana len retuen karo 

def remove_same_letter(s):
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right and s[left] == s[right]:
            left += 1
            right -= 1
    return right - left + 1

print(remove_same_letter("cacaabac"))

# 15. DI String Match
# Input: "IDID"
# Output: [0, 4, 1, 3, 2]

def DI_string(s):
    s = list(s)
    left = 0
    right = len(s)
    result = []

    for char in s:
        if char == "I":
            result.append(left)
            left += 1
        else:
            result.append(right)
            right -= 1

    result.append(left)
    return result

print(DI_string("IDID"))

# **16. Squares of a Sorted Array**
# Input: `[-4, -1, 0, 3, 10]`
# Output: `[0, 1, 9, 16, 100]`

def square_array(arr):
    left = 0
    right = len(arr) - 1
    result = []
    pos = 0

    while left <= right:
        left_sq = arr[left] ** 2
        right_sq = arr[right] ** 2

        if left_sq > right_sq:
            result.append(left_sq)
            left += 1
        else:
            result.append(right_sq)
            right -= 1

    return result[::-1]

print(square_array([-4, -1, 0, 3, 10]))
         



