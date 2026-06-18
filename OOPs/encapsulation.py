# P1 — Easy
# Person class banao — name public, _email protected, __password private. Getter + setter banao __password ke liye. Password change karo setter se.

# class person:
#     def __init__(self,name,email,password):
#         self.name = name
#         self._email = email
#         self.__password = password

#     def get_pass(self):
#         return self.__password
    
#     def set_pass(self , chng_pass):
#         if chng_pass == "abc123":
#             self.__password = "123abc"
#         else:
#             print("invalid password")
            
# p1 = person("kalpesh","kalpeshbhure01@gmail.com","abc1243")
# print(p1.get_pass())
# p1.set_pass("2222")
# print(p1.get_pass())


# P2 — Medium
# BankAccount class — __balance private. Methods:
# deposit(amount) → amount > 0 tabhi add
# withdraw(amount) → balance kam nahi hona chahiye
# @property balance → balance return kare

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,ammount):
        if ammount > 0:
            self.__balance += ammount
        else:
            print("invalid ammount")

    def withdraw(self,ammount):
        if ammount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= ammount
          
    @property
    def balance(self):
        return self.__balance
    
bank = BankAccount(4000)
bank.deposit(1000)
bank.withdraw(2000)
print(bank.balance)

    
