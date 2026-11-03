# Code: Temperature class bana. celsius property + fahrenheit computed read-only property. Celsius < -273.15 → ValueError.

# class Temperature():
#     def __init__(self,celcius):
#         self._celsius = celcius

#     @property
#     def celcius(self):
#         return self._celcius

#     @celcius.setter
#     def celcius(self,fahrenheit):
#         if fahrenheit < -273.15:
#             raise ValueError("valueError")
#         self._celcius = fahrenheit

#     @celcius.deleter
#     def celcius(self):
#         del self._celcius

# p1 = Temperature(100)
# p1.celcius(200)
# print(p1.celcius)
# p1.celcius(-300)

# # Student class banao (name, roll_no, marks), display() aur is_pass() (marks >= 40) ke saath.

class student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        return f"name : {self.name}\n roll_no : {self.roll_no}\n marks: {self.marks}"

    def is_pass(self):
        return self.marks >= 40
        

s = student("kalpesh" , 89 , 99)
print(s.display())
print(s.is_pass())

# Animal class → Dog class banao super() use karke. Dog mein extra attribute breed ho.

class  animal:
    def __init__(self,name):
        self.name = name

class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

d = dog("tommy","labro")
print(d.name,d.breed)

# Shape → Circle aur Rectangle, dono mein area() override karo.
import math
class shape:
    def area(self):
        raise NotImplementedError("class must have radius")

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

s = [circle(10), rectangle(20,35)]

for shape in s:
    print(shape.area())

# BankAccount banao: private __balance, deposit(), withdraw() (overdraft nahi), get_balance().
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amt):
        if amt <= 0:
            raise ValueError("invalid ammount")
        self.__balance += amt

    def withdraw(self,amt):
        if amt > self.__balance:
            raise ValueError("greater than balance")
        self.__balance -= amt

    @property
    def get_balance(self):
        return self.__balance
    

b = BankAccount(1000)
b.deposit(500)
b.withdraw(200)
print("amount : ", b.get_balance)


    
    