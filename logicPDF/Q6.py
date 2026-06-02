#Calculate and print the sum of the first n natural numbers
n = int(input("Enter first n natural num to get sum: "))
count = 1
sum1 = 0
while count <= n:
    sum1 = sum1 + count
    count += 1  
print(sum1)    
    