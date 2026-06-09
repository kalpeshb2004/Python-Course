#armstrong number checking
n = int(input("Enter a number here: "))
real_no = n
temp = 0
digits = 0
while n > 0:
    temp = n % 10
    digits = digits + (temp ** len(str(real_no)))
    n = n // 10

if digits == real_no:
    print("its armstrong number")
else:
    print("its not armstrog number")    
    