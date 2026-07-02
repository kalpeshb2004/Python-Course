# P1 — Easy
# Calculator banao — user se 2 numbers aur operator lo. Handle karo:

# ZeroDivisionError — division ke liye
# ValueError — galat input ke liye

# try:
#     a = int(input("enter a value: "))
#     b = int(input("inter b value: "))
#     result = a / b
# except ZeroDivisionError:
#     print("value shouldent be -ve or zero")
# except ValueError:
#     print("value must be integer")

# P2 — Medium
# User se file name lo. File padho aur print karo. Handle karo:

# FileNotFoundError — file nahi mili
# PermissionError — access nahi
# finally me print karo "Operation complete"

# filename = input("enter a file name : ")

# try:
#     with open(filename,"r") as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print("error: filke not found")
# except PermissionError:
#     print("error: you dont have a permission to open this file")
# finally:
#     print("operation complete")

