#Calculate and print the factorial of a given number.

n = int(input("enter a num to get factorial: "))
i = n
fact = 1

while i > 0:
    fact = fact * i
    i = i-1
print(fact)    