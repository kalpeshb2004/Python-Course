n = int(input())
lst = [n**2 if n%2==0 else n**3 for n in range(n)]
print(lst)