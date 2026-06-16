# P1 — Easy
# Student class banao. Attributes: name, age, marks. Method: introduce() jo print kare —
# "Mera naam Raj hai, age 20, marks 95"

# class student:
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
    
#     def introduce(self):
#         print(f'Mera name {self.name} hai, age {self.age}, marks {self.marks}')

# std1 = student("Raj",20,95)

# std1.introduce()

# P2 — Easy-Medium
# BankAccount class banao. Attributes: owner, balance. Methods:
# deposit(amount) → balance badhao
# withdraw(amount) → balance ghataao (balance kam ho toh "Insufficient funds")
# show_balance() → balance print karo

# class bankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self,amount):
#         self.balance += amount
    
#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")
    
#     def show_balance(self):
#         print(f'balance: {self.balance}')

# bal1 = bankAccount("kalpesh",100)

# bal1.deposit(500)
# bal1.withdraw(200)
# bal1.show_balance()

# P3 — Medium
# Rectangle class banao. Attributes: length, width. Methods:
# area() → length × width
# perimeter() → 2 × (length + width)
# is_square() → True/False (length == width)

# P4 — Hard

# Library class banao. Attributes: books (list). Methods:
# add_book(title) → list me add
# remove_book(title) → list se hatao
# search_book(title) → mila toh "Found" nahi toh "Not found"
# show_all() → sab books print karo

# class Library:
#     def __init__(self,book):
#         self.book = []

#     def add_book(self,title):
#         self.book.append(title)
    
#     def remove_book(self,title):
#         self.book.remove(title)
    
#     def serach_book(self,title):
#         if title in self.book:
#             print("Found")
#         else:
#             print("Not Found")
    
#     def show_all(self):
#         print(f'Books: {self.book}')

# lbr = Library("forest")

# lbr.add_book("jungle")
# lbr.add_book("mangle")
# lbr.add_book("dangal")
# lbr.remove_book("dangal")
# lbr.serach_book("jungle")
# lbr.show_all()


        


