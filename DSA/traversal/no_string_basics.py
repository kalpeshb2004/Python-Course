# Sum of digits — Number ka har digit nikal ke sabko jodna hai.
# Input: 12345 → Output: 15 (1+2+3+4+5)

def sum(value):
    result = 0

    while value > 0:
        result += value % 10
        value //= 10
    return result

print(sum(12345))

# Reverse digits — Number ke digits ka order ulta karna hai.
# Input: 12345 → Output: 54321
def reverse(value):
    result = 0
    while value > 0:
        digit = value % 10
        result = result * 10 + digit
        value = value // 10
    return result

print(reverse(12345))

# Palindrome number — Number ko reverse karke check karna hai ki original jaisa hi hai kya.
# Input: 121 → Output: True (reverse bhi 121 hai)
# Input: 123 → Output: False (reverse 321 hai, match nahi)

def palindrome(value):
    result = 0
    original = value

    while value > 0:
        digit = value % 10
        result = result * 10 + digit
        value = value // 10

    return result == original

print(palindrome(121))

# Harshad number — Digit sum nikalo, check karo original number us sum se poora divide hota hai kya (remainder 0).
# Input: 18 → digit sum=9, 18%9=0 → Output: True

def harshad(value):
    result = 0
    original = value
    while value > 0:
        result += value % 10
        value //= 10
    return original % result == 0

print(harshad(18))

# Prime number — Check karo number sirf 1 aur khud se hi divide hota hai, aur koi number se nahi.
# Input: 17 → Output: True (koi bhi 2 se 16 tak divide nahi karta)
# Input: 15 → Output: False (3 aur 5 se divide hota hai)


def prime(value):
    if value <= 1:
        return False
    for x in range(2, int(value**0.5) + 1):
        if value % x == 0:
            return False
    return True

print(prime(16))

# perfect no logic :
# agar no ke devisors ka sum no se match hota he o perfect no he
# ex = 28 , 1+2+4+7+14 = 28 , 28==28 match 

def perfect(value):
    if value <= 0:
        return False
    result = 0
    original = value
    for x in range(1, value):
        if value % x == 0:
            result += x
    return original == result
print(perfect(28))

# Count vowels and consonants — String ke har character ko check karo, vowel hai ya consonant, dono ka count rakho.
# Input: "hello world" → Output: Vowels=3, Consonants=7

def vowels_consonent(str):
    consonent = 0
    vowels = 0
    for x in str:
        if x.lower() in "aeiou":
            vowels += 1
        elif x.isalpha():
            consonent += 1
    return f"vowels = {vowels} , consonent = {consonent}"

print(vowels_consonent("hello world"))

# Count words in a sentence — Sentence ko space se split karke words ginne hai.
# Input: "I love coding" → Output: 3

def count_words(str):
    result = 0
    str = str.split(" ")
    for x in str:
        result += 1
    return result
print(count_words("I love coding"))

# Uppercase/lowercase (bina built-in) — Har character ka case badalna hai without using .upper()/.lower().
# Input: "Hello" → Output: "HELLO"

def upper_lower(str):
    result = ""
    for x in str:
        if "a" <= x <= "z":
            result += chr(ord(x) - 32)
        else:
            result += x
    return result
print(upper_lower("Hello"))

# Replace a character — String me diya gaya character dhundo, use naye character se badlo (bina built-in replace).
# Input: "banana", find="a", replace="o" → Output: "bonono"

def replace(str ,find, replace):
    result = ""

    for x in str:
        if x == find:
            result += replace
        else:
            result += x
    return result

print(replace("banana", "a", "o"))

# Count characters (bina len()) — String ke total characters gino bina len() use kiye, loop se.
# Input: "hello" → Output: 5

def count(str):
    count = 0

    for x in str:
        count += 1

    return count
print(count("hello"))

# Check if string starts/ends with substring — String ka shuru ya end diye gaye substring se match karta hai kya check karo.
# Input: "hello.txt", suffix=".txt" → Output: True

# Find longest word in sentence — Sentence ko words me todo, sabse lamba word dhundo.
# Input: "I love programming" → Output: "programming"

def longest(str):
    str = str.split(" ")
    longest = " "
    for x in str:
        if len(x) > len(longest):
            longest = x
    return longest

print(longest("I love programming"))

# String compression — Consecutive same characters ko character+count me convert karo.
# Input: "aabcccccaaa" → Output: "a2b1c5a3" (aa→a2, b→b1, ccccc→c5, aaa→a3)

