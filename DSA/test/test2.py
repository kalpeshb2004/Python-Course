# **Q1.** Given a string, return `True` if it reads the same forward and backward after removing all non-alphanumeric characters and ignoring case. Otherwise return `False`.

# Input: `"Was it a car or a cat I saw?"`

# Output: `True`

def valid_palindrom(str):
    left = 0
    right = len(str) - 1

    while left < right:
        while left < right and not str[left].isalnum():
            left += 1
        while left < right and not str[right].isalnum():
            right -= 1

        if str[left].lower() != str[right].lower():
            return False
        
        left += 1
        right -= 1
    return True
print(valid_palindrom("Was it a car or a cat I saw?"))

# **Q2.** Given a string, return the index of the first character that appears only once. If there is none, return `-1`.

# Input: `"loveleetcode"`

# Output: `2`

def first_occurence(s):
    freq = {}
    slow = 0

    for ch in s:
        freq[ch] = freq.get(ch , 0) + 1

    for index, ch in enumerate(s):
        if freq[ch] == 1:
            return index 
    return -1

print(first_occurence("loveleetcode"))

# **Q3.** Given two strings, merge them by adding letters in alternating order, starting with the first string. If one string is longer, append its remaining letters at the end.

# Input: `"ab", "pqrs"`

# Output: `"apbqrs"`

def merge_alternate(str1,str2):

    i = 0
    result = []
    while i < len(str1) and i < len(str2):
        result.append(str1[i])
        result.append(str2[i]) 
        i += 1

    result.extend(str1[i:])
    result.extend(str2[i:])
    return "".join(result)

print(merge_alternate("ab","pqrs"))

# **Q4.** Given an array and a value, remove all occurrences of that value and return the remaining elements in their original order.

# Input: `[0,1,2,2,3,0,4,2]`, `val = 2`

# Output: `[0,1,3,0,4]`

def remove_arr(arr,val):
    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != val:
            arr[slow] = arr[fast]
            slow += 1

    return arr[:slow]

print(remove_arr([0,1,2,2,3,0,4,2],2))

# **Q5.** Given an array of integers and a target, return the indices of the two numbers whose sum equals the target.

# Input: `[3,2,4]`, `target = 6`

# Output: `[1,2]`

def two_sum(arr,target):
    seen = {}

    for i in range(len(arr)):
        total = target - arr[i]
        if total in seen:
            return [seen[total] , i]
        seen[arr[i]] = i
    return -1
print(two_sum([3,2,4],6))

# **Q6.** Given a sorted array that may contain negative numbers, return an array of the squares of each number, also sorted in ascending order.

# Input: `[-5,-3,0,2,4]`

# Output: `[0,4,9,16,25]`

def sorte_sqr(arr):
    result = []
    left = 0
    right = len(arr) - 1

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

print(sorte_sqr([-5,-3,0,2,4]))

# **Q7.** Given an array and an integer `k`, return the maximum sum of any `k` consecutive elements.

# Input: `[2,1,5,1,3,2]`, `k = 3`

# Output: `9`

def sliding_sum(arr,k):
    n = len(arr)
    if n < k:
        return 0

    window_sum = sum(arr[:k])
    max_window = window_sum

    for i in range(k,n):
        window_sum += arr[i] - arr[i-k]
        max_window = max(max_window,window_sum)
    return max_window

print(sliding_sum([2,1,5,1,3,2],3))

# **Q8.** Given a positive integer, return `True` if the sum of the digits of its square equals the number itself. Otherwise return `False`.
# Input: `9`
# square = 81
# sum = 8 + 1 = 9
# input == sum
# return True

# Output: `True`

def number(num):
    square = num ** 2
    result = 0

    while square > 0:
        digit = square % 10
        result += digit
        square = square // 10

    if result != num:
        return False
    
    return True

print(number(9))

