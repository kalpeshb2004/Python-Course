#Calculate the sum of all even numbers from 1 up to n.

n = int(input("enter number to get of all even num sum: "))
i = 1
total = 0
while i <= n:
    if i % 2 == 0:
        total = total + i
    i = i + 1
print(total)    