def sort_sqr(arr):
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
    
print(sort_sqr([-5,-3,0,2,4]))