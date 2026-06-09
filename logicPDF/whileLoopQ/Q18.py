# Check whether the given number is a prime number.

n = int(input("enter a number check prime or not: "))
i = 2
while i < n:
    if n % i == 0:
        print("not prime")
        break
    i+=1
else:
    print("prime")    
