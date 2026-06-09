# Print all prime numbers between 1 and 100.

n = int(input("Enter a number to print prime: "))
num = 2  # 0 and 1 prime nahi he so num=2 liya
while num <= n: #outer loop 2 se n tak value print karega
    i = 2  # 0 and 1 prime nahi he so i=2 liya , i divisble no check karega
    prime = True 

    while i < num: # if ex num=7 he to i sirf 2 to 6 tak loop print karega devisble check karne ke liye 
        if num % i == 0: #devisible check karega 
            prime = False # even hua to false 
            break
        i+=1

    if prime: #true hua to print
        print(num)
    num += 1    

