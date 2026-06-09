# Calculate the sum of all odd numbers from 1 up to n.

n = int(input("Enter a number to get odd num sum: "))
i = 1
total = 0

while i <= n:
    if not i % 2 == 0:
        total = total + i
    i = i+1
print(total)