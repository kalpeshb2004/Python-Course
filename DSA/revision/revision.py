# Opposite End → Reverse string, two Sum, Palindrome after 1 removal
# Same Direction → Move Zeros, Remove Duplicates, Merge Sorted Arrays
# Hashing → Two Sum, Anagram, First Non-Repeating

def reverse(str):
    str = list(str)
    left = 0
    right = len(str) - 1

    while left < right:
        str[left],str[right] = str[right], str[left]
        left += 1
        right -= 1

    return "".join(str)
print(reverse("kalpesh")) 

def palindrome_1removal(str):
    str = list(str)
    left = 0
    right = len(str) - 1
    

    while left < right:
        if str[left] != str[right]:
            temp = str.copy()
            temp.pop(left)

            if temp == temp[::-1]:
                return True

            temp = str.copy()
            temp.pop(right)

            if temp == temp[::-1]:
                return True
            return False
        left += 1
        right -= 1
    return True

print(palindrome_1removal("abca"))

            
# two sum
# arr = [1, 2, 4, 7, 11, 15], target = 15

def two_sum(arr,target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return arr[left],arr[right]
        if total < target:
            left += 1
        if total > target:
            right -= 1
    return False  
print(two_sum([1, 2, 4, 7, 11, 15],15))
    
# Same Direction → Move Zeros, Remove Duplicates, Merge Sorted Arrays

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

print(move_zero([0,1,0,1,0,1]))  

# Input:  arr = [1, 1, 2, 2, 3, 4, 4]
# Output: [1, 2, 3, 4]   (length = 4)

def dupicates(arr):
    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != arr[fast-1]:
            arr[slow] = arr[fast]
            slow += 1
    return arr[:slow]

print(dupicates([1, 1, 2, 2, 3, 4, 4]))

# Merge Sorted Arrays
# input : [1,2,3,4] , [5,6,7,8,9]
# output : [1,2,3,4,5,6,7,8,9]

def merge_sorted(arr1,arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(result) == 0 or arr1[i] != result[-1]:
                result.append(arr1[i])
            i += 1
        else:
            if len(result) == 0 or arr2[j] != result[-1]:
                result.append(arr2[j])
            j += 1
    while i < len(arr1):
        if len(result) == 0 or arr1[i] != result[-1]:
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if len(result) == 0 or arr2[j] != result[-1]:
            result.append(arr2[j])
        j += 1

    return result

print(merge_sorted([1,2,3,4],[5,6,7,8,9])) 

# Hashing → Two Sum, Anagram, First Non-Repeating

# anagram listen and silent true 
