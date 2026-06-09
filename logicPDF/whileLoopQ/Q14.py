#sum of gitis of given number

n = int(input("enter a number"))

temp = 0

while n>0:
    digits = n % 10
    temp = temp + digits
    n = n // 10

print(temp)