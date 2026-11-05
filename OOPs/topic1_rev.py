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

# ABC use karke Payment abstract class banao, pay() abstract method ke saath. UPI aur Card classes banao.

from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amt,money):
        pass

class upi(payment):
    def __init__(self,amt):
        self.amt = amt

    def pay(self):
        return f"amount has paid by upi : {self.amt}"

class cart(payment):
    def __init__(self,amt):
        self.amt = amt

    def pay(self):
        return f"amount has paid by cart : {self.amt}"

s = [upi(200),cart(400)]
for shape in s:
    print(shape.pay())

# Employee class mein @classmethod (e.g. string “Ravi-5000” se object banao) aur @staticmethod (e.g. is_workday(day)).

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls,stri_form):
        name , salary = stri_form.split("-")
        return cls(name,int(salary))

    @staticmethod
    def is_workday(day):
        return day.lower() not in ("saturday" , "sunday")

    def display(self):
        return f"name : {self.name}\n salary : {self.salary}"

e1 = employee("kalpesh" , 150000)
e2 = employee.from_string("kalpesh-150000")

print(e1.display())
print(e2.display())

print(employee.is_workday("monday"))
print(employee.is_workday("saturday"))


a = [1,2,2,3,45,44,4,4,4,5]
print(list(dict.fromkeys(a)))


def duplicate(arr):
    slow = []
    for fast in range(len(arr)):
        if arr[fast] not in slow:
            slow.append(arr[fast])
    return slow
print(duplicate([11,11,2,2,2,2,3,4,4,5,4]))

def frequency(lst):
    freq = {}
    for ch in lst:
        freq[ch] = freq.get(ch,0) + 1
    return freq

print(frequency([11,11,2,2,2,2,3,4,4,5,4]))

# Do list ke common elements nikaal.
def common(lst1,lst2):
    lst11 = set(lst1)
    lst22 = set(lst2)
    return (lst11 & lst22)
print(common([1,1,1,2,2,2,3,3,3,4,4,4],[1,1,1,2,2,2]))

dict2 = {"name" : "kalpesh"}
dict3 = {"city" : "jayesh"}
new_dict = dict2 | dict3
print({**dict2,**dict3})
print(new_dict)
dict2.update(dict3)
print(dict2)


