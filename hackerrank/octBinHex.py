def print_formatted(number):
    width = len(bin(number)) - 2  # width of binary form of 'number', minus the '0b' prefix
    for i in range(1, number + 1):
        dec = str(i)
        octal = format(i, 'o')
        hexa = format(i, 'X')   # capital X for uppercase hex letters
        binary = format(i, 'b')
        print(dec.rjust(width), octal.rjust(width), hexa.rjust(width), binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)