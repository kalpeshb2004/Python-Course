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
        
class Student:
    def __init__(self):
        self.subject = []
        self.__marks = []

    def add_marks(self, subject, mark):
        if 0 <= mark <= 100:
            self.subject.append(subject)
            self.__marks.append(mark)
        else:
            print("Invalid marks!")

    @property
    def average(self):
        return sum(self.__marks) / len(self.__marks)

    @property
    def grade(self):
        avg = self.average
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

    def __str__(self):
        return f'Subjects: {self.subject}\nMarks: {self.__marks}\nAverage: {self.average}\nGrade: {self.grade}'


s1 = Student()
s1.add_marks("Maths", 85)
s1.add_marks("Science", 92)
s1.add_marks("English", 78)
print(s1)
        
        
