def print_formatted(number):
   for i in range(1,n+1):
    dec = i
    octal = format(i,'o')
    hexa = format(i,'x')
    binary = format(i,'b')
    print(dec,"\t",octal,"\t",hexa,"\t",binary)
   return number
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)