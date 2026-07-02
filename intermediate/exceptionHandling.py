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

# P3 — Medium
# Custom Exception banao InsufficientFundsError. BankAccount class — withdraw(amount) me raise karo agar balance kam ho. Try-except se handle karo.

# class InsufficientFundsError(Exception):
#     pass

# def withdraw(ammount):
#     if ammount < 500:
#         raise InsufficientFundsError("Balance of bank account is low")
#     if ammount > 100000:
#         raise InsufficientFundsError("balance limit existed")
#     return f"withdrawal has initiated: {ammount}"

# try:
#     print(withdraw(2222000))
# except InsufficientFundsError as e:
#     print(f"error: {e}")

# P4 — Hard
# StudentDatabase class — JSON file se kaam kare. Har method me proper exception handling:

# add_student() → duplicate name → custom DuplicateError
# find_student() → nahi mila → KeyError handle
# update_marks() → marks 0-100 ke bahar → custom InvalidMarksError
# delete_student() → nahi mila → handle karo

