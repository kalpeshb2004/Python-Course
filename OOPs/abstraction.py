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

# process_payment(creditcard(), 5000)
# process_payment(upi(), 1000)
# process_payment(cash(), 3000)


# P3 — Medium
# Employee abstract class — @abstractmethod: calculate_salary(). 3 child class:
# FullTime(base_salary) → base salary
# PartTime(hours, rate) → hours × rate
# Freelancer(projects, rate_per_project) → projects × rate

# from abc import ABC , abstractmethod
# class employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class fulltime(employee):
#     def calculate_salary(self,base_salary):
#         return base_salary

# class parttime(employee):
#     def calculate_salary(self,hour,rate):
#         print(f'hours per rate: {hour * rate}$')

# class freelancer(employee):
#     def calculate_salary(self,projects,rate_per_project):
#         print(f'rates per project: {projects * rate_per_project}$')

# f1 = fulltime()
# print(f1.calculate_salary(100000))

# p1 = parttime()
# p1.calculate_salary(1,35)

# fr1 = freelancer()
# fr1.calculate_salary(2,500)


#  P4 — Hard
# DatabaseConnection abstract class — @abstractmethod: connect(), disconnect(), execute(query). 2 child: MySQLConnection, MongoDBConnection. Har ek apna message print kare. run_query(db, query) function banao jo connect → execute → disconnect kare.

# from abc import ABC ,abstractmethod
# class DatabaseConnection(ABC):
#     @abstractmethod
#     def connect(self):
#         pass

#     @abstractmethod
#     def execute(self,query):
#         pass

#     @abstractmethod
#     def disconnected(self):
#         pass

# class MySQLConnection(DatabaseConnection):
#     def connect(self):
#         print("MySQLConnection connected")

#     def execute(self, query):
#         print(f'MySQL query executed: {query}')
    
#     def disconnected(self):
#         print("MySQL disconnected")

# class MongoDBConnection(DatabaseConnection):
#     def connect(self):
#         print("MongoDBConnection connected")

#     def execute(self, query):
#         print(f'MongoDB query executed: {query}')
    
#     def disconnected(self):
#         print("MongoDB disconnected")
    

# def run_query(db, query):
#     db.connect()
#     db.execute(query)
#     db.disconnected()

# run_query(MySQLConnection(),"SELECT * FROM")
# run_query(MongoDBConnection(), "db.users.find()")

# ✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️
# Revision example 1.1
# Project 1: Animal 

# Animal(ABC), abstract sound()
# Dog, Cat → sound implement
# Loop me sab ka sound() call

# Chhota hai. Pehle ye likh. Phir Payment, Shape.

# from abc import ABC , abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return f"bhow"
    
# class Cat(Animal):
#     def sound(self):
#         return f"meow"

# Animal = [Dog() , Cat()]
# for a in Animal:
#     print(a.sound())

# bina dekhe dobara likh. Phir Vehicle(ABC) (start(), Car, Bike) likh.

from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "car has started"

class Bike(Vehicle):
    def start(self):
        return "Bike has started"

Vehicles = [Car(),Bike()]
for v in Vehicles:
    print(v.start())

# Project: Payment System, example : 1.2 
# Task
# Payment(ABC): abstract pay(amount).
# Concrete method receipt(amount) (sab child ko mile, override nahi).
# Child: UPI, Card, NetBanking → pay() implement.
# Loop me sab call.
# Bonus: amount <= 0 → ValueError.
# Pehle khud likh

# Hint structure:

# Payment(ABC)
#  ├─ @abstractmethod pay(self, amount)
#  └─ receipt(self, amount)        # concrete
# UPI(Payment)     → pay
# Card(Payment)    → pay
# NetBanking(Payment) → pay

from abc import ABC , abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount): #abstract method
        pass

    def receipt(self, amount):
        return f"amount {amount} has paid vai comcrete" #concrete method

class UPI(Payment):
    def pay(self,amount):
        if amount <= 0:
            raise ValueError("insufficint UPI amount")
        return f"UPI amount {amount} has paid"

class Card(Payment):
    def pay(self,amount):
        if amount <= 0:
            raise ValueError("insufficint Card amount")
        return f"Card amount {amount} has paid"

class NetBanking(Payment):
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("insufficint Netbanking amount")
        return f"NetBanking amount {amount} has paid"

result = [UPI() , Card(), NetBanking()]
for r in result:
    print(r.receipt(1000))
    print(r.pay(500))

# example 1.3
# Project: Shape (Abstraction + Polymorphism)
# Task
# Shape(ABC): 2 abstract methods → area(), perimeter().
# Concrete method describe() → "Circle: area=78.5, perimeter=31.4" (parent me, sab reuse).
# Child: Circle(r), Rectangle(w, h), Triangle(a, b, c).
# Loop me sab ka describe() call.
# Bonus: negative/zero side → ValueError.

# Hint structure
# Shape(ABC)
#  ├─ @abstractmethod area()
#  ├─ @abstractmethod perimeter()
#  └─ describe()            # concrete, self.area() call kare

# Circle    → area, perimeter
# Rectangle → area, perimeter
# Triangle  → area (Heron), perimeter

# Formula
# Circle: π r², 2 π r
# Rectangle: w * h, 2 * (w + h)
# Triangle (Heron): s = (a+b+c)/2, area = (s(s-a)(s-b)(s-c)) ** 0.5

import math
from abc import ABC ,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return (f"{self.__class__.__name__}"
                f"area={self.area():.2f}, "
                f"perimeter={self.perimeter():.2f}, ")

class circle(shape):
    def __init__(self,r):
        if r <= 0:
            raise ValueError("radius should be larger than 0")
        self.r = r


    def area(self):
        return math.pi * self.r **2
    
    def perimeter(self):
        return 2 * math.pi * self.r

class reactangle(shape):
    def __init__(self,w,h):
        if w<=0 or h<=0:
            raise ValueError("w and h must be larger than 0")
        self.w,self.h = w,h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

class taringle(shape):
     def __init__(self,a,b,c):
         if min(a,b,c) <= 0 or a+b <= c or a+c <= b or b+c <= a:
             raise ValueError("a , b , c are incorrect value")
         self.a,self.b,self.c = a,b,c

     def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

     def perimeter(self):
        return self.a + self.b + self.c

result = [circle(5) , reactangle(10,4) , taringle(3,4,5)]
for r in result:
    print(r.describe())

      
         






