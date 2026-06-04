# Find and print the sum of the Fibonacci series up to n terms
n = int(input())
a = 0
b = 1
i = 0
temp = 0

while i<n: # <= mtlb 0 to n hota mtlb ek no extra , < me 0 to n-1 hota he mtlb exact n no 
     temp += a    # last me store ni karana warna a ki first original value add ni hoti updated hoti he to 1 no extra add hota he        
     c = a+b
     a = b
     b = c
     i+=1  
     print(temp)    

