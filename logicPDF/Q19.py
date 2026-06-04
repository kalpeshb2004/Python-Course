# Print the Fibonacci series up to n terms.
n = int(input())
a = 0
b = 1
i = 0
while i<n:
    print(a , end=" ") #
    c = a+b
    a=b
    b=c
    i+=1
