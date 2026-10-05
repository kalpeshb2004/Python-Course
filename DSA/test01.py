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