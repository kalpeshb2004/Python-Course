def LCM(a,b):
    big = max(a,b)
    num = big

    while num % a != 0 or num % b != 0:
        num += big
    return num
print(LCM(4,6))