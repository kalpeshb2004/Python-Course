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

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance

#     def deposit(self,ammount):
#         if ammount > 0:
#             self.__balance += ammount
#         else:
#             print("invalid ammount")

#     def withdraw(self,ammount):
#         if ammount > self.__balance:
#             print("Insufficient funds!")
#         else:
#             self.__balance -= ammount
          
#     @property
#     def balance(self):
#         return self.__balance
    
# bank = BankAccount(4000)
# bank.deposit(1000)
# bank.withdraw(2000)
# print(bank.balance)


# P3 — Medium
# Employee class — __salary private. @property use karo:
# salary getter → return kare
# salary setter → 0 se kam nahi ho sakta, 1000000 se zyada nahi
# annual property → salary × 12


# class employee:
#     def __init__(self,salary):
#         self.__salary = salary
    
#     @property
#     def salary(self):
#         return self.__salary
    
#     @salary.setter
#     def salary(self,amount):
#         if amount < 0 or amount > 1000000: 
#             print("invalid salary")

#     @property
#     def ann_property(self):
#         return self.__salary * 12

# emp = employee(100000)
# print(emp.salary)
# emp.salary = -4000000
# print(emp.ann_property)


# P4 — Hard
# Student class — __marks private (list of 3 subjects). Methods:
# add_marks(subject, mark) → 0-100 ke beech hi accept karo
# @property average → average calculate karo
# @property grade → A(90+), B(75+), C(60+), F(below 60)
# __str__ → sab info print karo
        
# class Student:
#     def __init__(self):
#         self.subject = []
#         self.__marks = []

#     def add_marks(self, subject, mark):
#         if 0 <= mark <= 100:
#             self.subject.append(subject)
#             self.__marks.append(mark)
#         else:
#             print("Invalid marks!")

#     @property
#     def average(self):
#         return sum(self.__marks) / len(self.__marks)

#     @property
#     def grade(self):
#         avg = self.average
#         if avg >= 90:
#             return "A"
#         elif avg >= 75:
#             return "B"
#         elif avg >= 60:
#             return "C"
#         else:
#             return "F"

#     def __str__(self):
#         return f'Subjects: {self.subject}\nMarks: {self.__marks}\nAverage: {self.average}\nGrade: {self.grade}'


# s1 = Student()
# s1.add_marks("Maths", 85)
# s1.add_marks("Science", 92)
# s1.add_marks("English", 78)
# print(s1)

# day 1 Of OOPs   
# encapsulation 1.1
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self,amt):
        if amt <= 0:
            raise ValueError("Invalid ammount")
        self.__balance += amt

    def withdraw(self,amt):
        if amt > self.__balance:
            raise ValueError("insufficiant balance")
        self.__balance -= amt

acc = BankAccount("kalpesh",1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)

# encapsulation 1.2
# Student:	_marks private, setter me 0-100 validation
class student:
    def __init__(self , name,marks):
        self.name = name
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,m):
        if not 0 <= m <= 100:
            raise ValueError("Marks should be in 0-100")
        self._marks = m

s = student("kalpesh",97)
s.marks = 96

# encapsulation 1.3
# Temperature:	celsius property + fahrenheit read-only computed

class tempreture:
    def __init__(self,celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self,value):
        if value < -275:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

t = tempreture(27)
print(t.celsius)
print(t.fahrenheit)

t.celsius = 100
print(t.fahrenheit)  

# encapsulation 1.4
# Wallet:	__balance, add(), spend(), spend > balance → error

class wallet:
    def __init__(self, balance=0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def add(self,add):
        if add <= 0:
            raise ValueError("insufficiant value")
        self.__balance = add

    def spend(self,spend):
        if spend > self.__balance:
            raise ValueError("not much balance to spend")
        self.__balance -= spend

w = wallet()
w.add(1000)
w.spend(400)
print(w.balance)

# encapsulation 1.5
# User Login	__password, check_password(), password getter nahi

class user_login:
    def __init__(self,username,password):
        self.username = username
        self.__password = password

    def check_password(self ,pwd):
        return pwd == self.__password

    def change_password(self,old ,new):
        if not self.check_password(old):
            raise ValueError("wrong password")
        if len(new) < 6:
            raise ValueError("need min 6 char")
        self.__password = new

u = user_login("kalpesh" ,"1234Kalpesh")
print(u.check_password("1234Kalpesh"))  
print(u.check_password("1234Kalp4e5tesh")) 
u.change_password("1234Kalpesh","1234kal")    
print(u.check_password("1234kal"))   

# encapsulation 1.6
# 5	Product	price setter (negative reject), discount() method

class product:
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,discount):
        if discount < 0:
            raise ValueError("negative discount rejected")
        self._price = discount 

    def discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Percent 0-100")
        return self._price * (100 - percent) / 100

p = product(1000)
print(p.discount(10))      # 900.0
p.price = 1200     

# 6	Counter	__count, sirf increment() / reset() se badle
# 7	Employee	__salary, raise_salary(%), direct set band
# 8	Stack	__items list private, push/pop/peek, bahar se list na dikhe
# 9	Library Book	__is_issued, issue() / return_book(), double issue error
# 10	Vending Machine	private stock + cash, buy(item, money)