def two_sum(arr,target):
    seen = {}
    for i in range(len(arr)):
        total = target - arr[i]
        if total in seen:
            return [arr[seen[total]] , arr[i]]
        seen[arr[i]] = i
    return -1
print(two_sum([1,2,3,2,4,5,1],7))
        