def reverse(str):
    str = list(str)
    left = 0
    right = len(str) -1

    while left < right:
        str[left], str[right] = str[right] , str[left]
        left += 1 
        right -= 1
    return "".join(str)

print(reverse("hello")) 

def reverse(str):
    result = ""
    for ch in str:
        result = ch + result 
    return result
print(reverse("hello")) 

def palindrom(str):
    str = list(str)
    left = 0
    right = len(str) -1

    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1

    return True
print(palindrom("naman"))
print(palindrom("kalpesh"))

def num_palindrome(num):
    original = num
    result = 0
    while num > 0:
        digit = num % 10
        result = result * 10 + digit
        num //= 10
    return original == result
print(num_palindrome(121))
print(num_palindrome(1211))

def num_reverse(num):
    result = 0
    while num > 0:
        digit = num % 10
        result = result * 10 + digit
        num //= 10
    return result
print(num_reverse(12345))
print(num_reverse(1211))


for i in range(2,20):
    for j in range(2,int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)

a,b = 0,1
for i in range(20):
    print(a,end=" ")
    a = b
    b = a + b

a,b = 0,1
while a <= 20:
    print(a,end=" ")
    a ,b = b, a + b

def perfect(num):
    total = 0
    for i in range(1,num):
        if num % i == 0:
            total += i
    return total == num
print(perfect(28))
print(perfect(12))

def sum_num(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    return sum
print(sum_num(12345))

def count_num(num):
    count = 0
    while num > 0:
        digit = num % 10
        count += 1
        num //= 10
    return count
print(count_num(12345))
print(count_num(12764363636363))

def reverse_words(sentence):
    words = sentence.split()
    left  = 0
    right = len(words) - 1

    while left < right:
        words[left] ,words[right] = words[right],words[left]
        left += 1
        right -= 1
    return " ".join(words)
print(reverse_words("me love python"))

def volwels_consonent(words):
    vowels = 0
    consonent = 0
    for word in words:
        if word in "aeiou":
            vowels += 1
        else:
            consonent += 1
    return f"vowels : {vowels}  consonent : {consonent}"

print(volwels_consonent("leetcodesgwesdsdfg"))

def freqency(str):
    freq = {}
    for ch in str:
        freq[ch] = freq.get(ch,0) + 1
    return freq
print(freqency("dgshgfjwsjedsasfsfgdfwsgdgasfdsfdfsv"))

def freqency(str):
    freq = {}
    for ch in str:
        freq[ch] = freq.get(ch,0) + 1

    result = {}
    for ch,count in freq.items():
        if count >= 2:
            result[ch] = count
    return result
print(freqency("dgshgfjwsjedsasfsfgdfwsgdgasfdsfdfsv"))

def duplicate(str):
    result = []
    for word in str:
        if word not in result:
            result.append(word)

    return "".join(result)
print(duplicate("sdfgsdfscadasdasdasd"))

def remove_duplicate(str):
    ste1 = set()
    ste2 = set()

    for ch in str:
        if ch in ste1:
            ste2.add(ch)
        else:
            ste1.add(ch)
    return ste1
print(remove_duplicate("sdgfdsdsdfwerrtfwe"))

# anagram : listen and silent are anagram (same char same length)
def anagram(str1,str2):
    if len(str1) != len(str2):
        return False

    freq = {}
    for ch in str1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in str2:
        freq[ch] = freq.get(ch, 0) - 1

    for count in freq.values():
        if count != 0:
            return False
    return True
print(anagram("listen","silent"))
print(anagram("listec","silent"))
print(anagram("dtgd","dgewshw"))

def first_non_repeat_char(str1):
    freq = {}
    for ch in str1:
        freq[ch] = freq.get(ch,0) + 1

    for ch,count in freq.items():
        if count == 1:
            return ch
    return -1
print(first_non_repeat_char("sdfsdfsdfcs"))

def largest_element(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] > result:
            result = arr[i]
    return result
print(largest_element([10,2,3,45,2,6]))

def smallest_element(arr):
    result = arr[0]
    for i in range(len(arr)):
        if arr[i] < result:
            result = arr[i]
    return result
print(smallest_element([10,2,3,45,3,2]))

def second_largest(arr):
    arr.sort()
    return arr[-2]
print(second_largest([10,2,3,45,3,2]))

def second_smallest(arr):
    arr.sort()
    return arr[1]
print(second_smallest([10,2,3,45,3,2]))

def sum_arr(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
print(sum_arr([10,2,3,45,3,2]))

def reverse(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left] , arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
print(reverse([3,432,1,33,3,2]))

def is_sorted(arr):
    for fast in range(1,len(arr)):
        if arr[fast] < arr[fast-1]:
            return False
    return True
print(is_sorted([1,2,3,4,5,6,7]))
print(is_sorted([2,31,4,134,2,21]))

def remove_duplicates(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] not in result:
            result.append(arr[i])
    return result
print(remove_duplicates([2,31,4,134,2,21,3,2,3,2,3,1,1]))

def missing_arr(arr):
    n = len(arr) + 1
    total_sum = sum(arr)
    expected_sum = n * (n + 1) / 2
    missing_num = expected_sum - total_sum
    return missing_num
print(missing_arr([1,2,4,5]))

def frequency_arr(arr):
    freq = {}
    for i in range(len(arr)):
        freq[arr[i]] = freq.get(arr[i] ,0) + 1
    return freq
print(frequency_arr([2,31,4,134,2,21,3,2,3,2,3,1,1]))

def common_ele_arr(arr1,arr2):
    ar1 = set(arr1)
    ar2 = set(arr2)
    return (ar1 & ar2)
print(common_ele_arr([1,2,3,4,5,23,1,1],[1,2,3,2,3,2]))

def merge_arr(arr1,arr2):
    i = 0
    result = []
    while i < len(arr1) and i < len(arr2):
        result.append(arr1[i])
        result.append(arr2[i])
        i += 1
    result.extend(arr1[i:])
    result.extend(arr2[i:])
    return result
print(merge_arr([1,2,3,4,5,23,1,1],[1,2,3,2,3,2]))

def move_zero(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow] = arr[fast]
            slow += 1

    while slow < len(arr):
        arr[slow] = 0
        slow += 1
    return arr[:slow]
print(move_zero([1,0,2,3,0,3,1,0,5,2,0]))

def two_sum(arr,target):
    seen = {}
    for i in range(len(arr)):
        total = target - arr[i]
        if total in seen:
            return [arr[seen[total]] , arr[i]]
        seen[arr[i]] = i
    return -1
print(two_sum([1,2,3,2,4,5,1],7))


        



            





            


  



