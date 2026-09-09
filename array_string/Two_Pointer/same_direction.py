# **1. Move Zeros to End**
# Input: `[0, 1, 0, 3, 12]
# Output: `[1, 3, 12, 0, 0]

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


# **2. Remove Duplicates from Sorted Array (in-place)**

# Input: `[1, 1, 2, 2, 3]`

# Output: `[1, 2, 3]` (length 3)

def remove_duplicates(arr):
    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != arr[fast - 1]:
            arr[slow] = arr[fast]
            slow += 1

    return arr[:slow]

print(remove_duplicates([1, 1, 2, 2, 3]))

# **3. Remove Element (given value, in-place)**

# Input: `[3, 2, 2, 3]`, `val = 3`

# Output: `[2, 2]` (length 2)

def remove_element(arr,val):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != val:
            arr[slow] = arr[fast]
            slow += 1

    return arr[:slow]

print(remove_element([3, 2, 2, 3],3))

# **4. Remove Duplicates from Sorted Array II (at most 2 copies allowed)**

# Input: `[1, 1, 1, 2, 2, 3]`

# Output: `[1, 1, 2, 2, 3]`

def remove_duplicates2(arr):
    slow = 2
    for fast in range(2,len(arr)):
        if arr[fast] != arr[slow-2]:
            arr[slow] = arr[fast]
            slow += 1

    return arr[:slow]

print(remove_duplicates2([1, 1, 1, 2, 2, 3]))


# **5. Merge Two Sorted Arrays**

# Input: `arr1 = [1, 3, 5, 7]`, `arr2 = [2, 4, 6, 8]`

# Output: `[1, 2, 3, 4, 5, 6, 7, 8]`

# NORMAL CASE

def Merge_2_sortedArr(arr1,arr2):
     result = []
     i = 0
     j = 0

     while i < len(arr1) and j < len(arr2):
         if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
         else:
             result.append(arr2[j])
             j += 1

     result.extend(arr1[i:])  #bache hue element add kar raha he hamesha extend use karana 
     result.extend(arr2[j:])

     return result

print(Merge_2_sortedArr([1, 3, 5, 7],[2, 4, 6, 8]))
# ab yaha direct element big or small dekh ke insert ho rahe he duplicate allowed he koi restriction nahi he 


# **5. Merge Two Sorted Arrays**
# Input: `arr1 = [1,1,1,2,4,6,7]`, `arr2 = [1,2,3,6,7,8,9,10]`
# Output: `[1, 2, 3, 4, 5, 6, 7, 8,9,10]`
#advanced case (LeetCode problem)
#duplicate values allowed nahi he 

def merge_two_sorted_array(arr1,arr2):
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

print(merge_two_sorted_array([1,1,1,2,4,6,7],[1,2,3,6,7,8,9,10]))

# **6. Union of Two Sorted Arrays (no duplicates)**

# Input: `arr1 = [1, 3, 4, 5]`, `arr2 = [2, 3, 5, 6]`

# Output: `[1, 2, 3, 4, 5, 6]`

def union_array(arr1,arr2):
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

print(union_array([1, 3, 4, 5],[2, 3, 5, 6]))

# **7. Intersection of Two Sorted Arrays**

# Input: `arr1 = [1, 2, 4, 5, 6]`, 
#         `arr2 = [2, 3, 5, 7]`

# Output: `[2, 5]`

def intersection_array(arr1,arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result

print(intersection_array([1, 2, 4, 5, 6],[2, 3, 5, 7]))

# **8. Find Common Elements With Duplicates (two sorted arrays)
# Input: `arr1 = [1, 2, 2, 3]`, `arr2 = [2, 2, 4]`
# Output: `[2, 2]`

def common_elements(arr1,arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if len(result) == 0 or result[-1] == arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return result

print(common_elements([1, 2, 2, 3],[2, 2, 4]))

# **9. Is Subsequence (string check)**
# Input: `s = "abc"`, `t = "ahbgdc"`
# Output: `True`
    
def is_subsequence(s,t):
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

print(is_subsequence("abc","ahbgdc"))


            