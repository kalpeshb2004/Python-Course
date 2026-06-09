#palindrome

n = int(input("enter a number t check palindrome or not: "))
rev = 0
temp = n

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
    
if rev == temp:
    print("no is palindrom")
else:
    print("no is not palindrome")       