# 13. Palindrome After One Swap
# Input: [1, 2, 4, 2, 1]
# Output: True

def palindrome_one_after_swap(arr):
    left, right = 0, len(arr) - 1

    # jab tak match ho, dono pointer andar aao
    while left < right:
      if arr[left] == arr[right]:
        left += 1
        right -= 1
      else:
         break

    if left >= right:
        return True   # already palindrome, swap ki zarurat nahi

    # ek hi mismatch pair par swap try karo
    arr[left], arr[right] = arr[right], arr[left]
    return arr == arr[::-1]

print(palindrome_one_after_swap([1, 2, 4, 2, 1]))  # True
