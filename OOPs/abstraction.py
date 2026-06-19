# P1 — Easy
# Vehicle abstract class banao — @abstractmethod: start(), stop(). 2 child: Car, Bike. Dono me implement karo. Objects banao aur methods bulao.

# from abc import ABC , abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("car is started")
    
#     def stop(self):
#         print("car is stoped")
    
# class Bike(Vehicle):
#     def start(self):
#         print("Bike is started")

#     def stop(self):
#         print("Bike is stoped")

# c1 = Car()
# c1.start()
# c1.stop()

# b1 = Bike()
# b1.start()
# b1.stop()


# P2 — Medium
# Payment abstract class — @abstractmethod: pay(amount), validate(). 3 child: CreditCard, UPI, Cash. Har ek apne tarike se implement kare. process_payment(payment, amount) function banao.

# from abc import ABC , abstractmethod

# class payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass

#     @abstractmethod
#     def validate(self):
#         pass

# class creditcard(payment):
#     def pay(self,amount):
#         print(f'credit card se {amount} pay hua')
    
#     def validate(self):
#         print("creditcard validate hua")

# class upi(payment):
#     def pay(self,amount):
#         print(f'UPI se {amount} pay hua')
    
#     def validate(self):
#         print("UPI validate hua")

# class cash(payment):
#     def pay(self,amount):
#         print(f'cash se {amount} pay hua')
    
#     def validate(self):
#         print("cash validate hua")

# def process_payment(payment, amount):
#     payment.pay(amount)
#     payment.validate()

# C1 = creditcard()
# C1.pay(1000)
# C1.validate()

# u1 = upi()
# u1.pay(2000)
# u1.validate()

# c1 = cash()
# c1.pay(3000)
# c1.validate()

# process_payment(creditcard(), 5000)
# process_payment(upi(), 1000)
# process_payment(cash(), 3000)


# P3 — Medium
# Employee abstract class — @abstractmethod: calculate_salary(). 3 child class:
# FullTime(base_salary) → base salary
# PartTime(hours, rate) → hours × rate
# Freelancer(projects, rate_per_project) → projects × rate

from abc import ABC , abstractmethod
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class fulltime(employee):
    def calculate_salary(self,base_salary):
        return base_salary

class parttime(employee):
    def calculate_salary(self,hour,rate):
        print(f'hours per rate: {hour * rate}$')

class freelancer(employee):
    def calculate_salary(self,projects,rate_per_project):
        print(f'rates per project: {projects * rate_per_project}$')

f1 = fulltime()
print(f1.calculate_salary(100000))

p1 = parttime()
p1.calculate_salary(1,35)

fr1 = freelancer()
fr1.calculate_salary(2,500)

        
       
        






