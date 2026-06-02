#reverse number and print

num = int(input("enter  a number: "))
temp = 0
rev = 0

while num > 0:
    temp = num % 10 #it gives last digits
    rev = rev * 10 + temp 
    num = num // 10

print(rev)