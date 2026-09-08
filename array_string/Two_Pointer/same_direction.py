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

