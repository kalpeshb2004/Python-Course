# P2 — Medium
# mypackage banao — 2 modules:

# string_utils.py → reverse(), uppercase(), word_count()
# number_utils.py → is_even(), factorial(), is_prime()
# main.py me dono import karke test karo.

def is_even(num):
    return num % 2 == 0

def factorail(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i 
    return fact

def is_prime(n):
    if n < 2:              # 0, 1 prime nahi
        return False
    
    for i in range(2, n):  # 2 se n-1 tak check karo
        if n % i == 0:     # koi bhi divide kare → prime nahi
            return False
    
    return True            # koi divide nahi kiya → prime hai