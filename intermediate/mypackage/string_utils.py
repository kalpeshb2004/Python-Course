# P2 — Medium
# mypackage banao — 2 modules:

# string_utils.py → reverse(), uppercase(), word_count()
# number_utils.py → is_even(), factorial(), is_prime()
# main.py me dono import karke test karo.

def reverse(str):
    return str[::-1]

def uppercase(str):
    return str.upper()

def wordcount(str):
    count = 0
    for char in str:
        count += 1
    return count
