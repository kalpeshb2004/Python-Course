# 15 problems
# input : [1,1,2,2,3,3,4,4]
# Output : [1,2,3,4]

def duplicate(arr):
    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != arr[slow-1]:
            arr[slow] = arr[fast]
            slow += 1

    return arr[:slow]

print(duplicate([1,1,2,2,3,3,4,4]))

# Q1. Reverse a string without using built-in reverse function.
# Input: "hello"

def  reverse(str):
    str = list(str) 
    left = 0
    right = len(str) - 1

    while left < right:
        str[left] , str[right] = str[right] , str[left]
        left += 1
        right -= 1

    return "".join(str)

print(reverse("kalpesh")) 


# Q2. Check whether a given string is a palindrome.
# Input: "madam"
def  reverse(str):
    str = list(str) 
    original = str
    left = 0
    right = len(str) - 1

    while left < right:
        if str[left] == str[right]:
            return True
        left += 1
        right -= 1

    return False

print(reverse("madam")) 

# Q3. Given a string, check if it is a valid palindrome, ignoring spaces, punctuation, and case.
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

# Q4. Given a sorted array, find a pair of elements whose sum equals a given target.
# Input: arr = [1, 2, 3, 4, 6], target = 6

def arr(arr,target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return arr[left] , arr[right]
        elif total < target:
            left += 1
        elif total > target:
            right -= 1

print(arr([1,2,3,4,6],6))

# Q5. Reverse the vowels of a given string.
# Input: "leetcode"

def rev_vowles(str):
    str = list(str)
    left = 0
    right = len(str) - 1

    while left < right:
        while left < right and str[left] not in "aeiou":
            left += 1
        while left < right and str[right] not in "aeiou":
            right -= 1

        str[left] , str[right] = str[right] , str[left]
        left +=1
        right -= 1
    return "".join(str)

print(rev_vowles("leetcode"))


# Q7. Given an array of 0s and 1s, move all zeros to the end while maintaining the relative order of non-zero elements.
# Input: [0, 1, 0, 3, 12]

def move_zero(arr):
    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow] = arr[fast]
            slow += 1

    while slow < len(arr):
        arr[slow] = 0
        slow += 1
    return arr

print(move_zero([0, 1, 0, 3, 12]))

# Q8. Remove duplicates from a sorted array in-place and return the resulting array.
# Input: [1, 1, 2, 2, 3]

def duplicate(arr):
    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != arr[fast-1]:
            arr[slow] = arr[fast]
            slow += 1
    return arr[:slow]

print(duplicate([1,1,2,2,3,3,4,4]))

# Q9. Merge two sorted arrays into a single sorted array.
# Input: arr1 = [1, 3, 5, 7], arr2 = [2, 4, 6, 8]

def sorted_arry(arr1,arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
          if arr1[i] < arr2[j]:
              result.append(arr1[i])
              i += 1
          else:
              result.append(arr2[j]) 
              j += 1
    return result

print(sorted_arry([1, 3, 5, 7],[2, 4, 6, 8]))

# Q10. Find the union of two sorted arrays (no duplicates in output).
# Input: arr1 = [1, 3, 4, 5], arr2 = [2, 3, 5, 6]
def union(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if len(result) == 0 or arr1[i] != result[-1]:
                result.append(arr1[i])
            i += 1
        else:
            if len(result) == 0 or arr2[j] != result[-1]:
                result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

print(union([1, 3, 4, 5],[2, 3, 5, 6]))

# Q11. Given a number, check whether it is a Harshad number.
# Input: 18
# 1+8 = 9 , 18%9 == 0

def harshad(num):
    original = num
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    if original % total == 0:
        return f"{original} is harshad number"
    else:
        return f"{original} is not harshad number"
    
print(harshad(18))
