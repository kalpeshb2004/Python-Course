# perfect number

n = int(input("Enter a number: "))
temp = n
sum1 = 0
i = 1

while i < n:
    if n % i == 0:
        sum1 += i
    i += 1
if sum1 == temp:
    print("its a perfect number")
else:
    print("its not perfect number")    
