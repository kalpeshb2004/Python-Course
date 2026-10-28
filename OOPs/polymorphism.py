# P1 — Easy (Overriding)
# Employee class — work() method → "Employee kaam kar raha hai". 3 child classes: Developer, Designer, Manager. Har ek work() override kare apne kaam ke saath. Loop me sab ka work() bulao.

# class employee:
#     def work(self):
#         print("Employee kaam kar raha hai")

# class developer(employee):
#     def work(self):
#         print("developer kaam kar raha hai")

# class designer(employee):
#     def work(self):
#         print("designer kaam kar raha hai")

# class manager(employee):
#     def work(self):
#         print("manager kaam kar raha hai")

# workers = [developer() , designer() , manager()]
# for w in workers:
#     w.work()

# P2 — Medium (Overloading)
# Calculator class — multiply() method jo:
# 1 number → square kare
# 2 numbers → multiply kare
# 3 numbers → teeno multiply kare

# class calculator:
#     def multiply(self,*args):
#         if len(args) == 1:
#             print(f'sqaure: {args[0] * args[0]}')
#         elif len(args) == 2:
#             print(f'sqaure: {args[0] * args[1]}')
#         elif len(args) == 3:
#             print(f'sqaure: {args[0] * args[1] * args[2]}')
        
# c = calculator()
# c.multiply(10)
# c.multiply(10,20)
# c.multiply(10,20,30)

# P3 — Medium (Operator Overloading)
# Student class — name, marks. + operator override karo — do students ke marks add ho jaye aur naya Student return kare. > operator — marks compare kare. __str__ — "Name: Raj, Marks: 95" print kare.

# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def __add__(self, other):
#         return student("marks:",self.marks + other.marks)
    
#     def __gt__(self, other):
#         return self.marks > other.marks
    
#     def __str__(self):
#         return f'name: {self.name}, marks: {self.marks}'  
        
# std1 = student("Raj" ,95)
# std2 = student("jayesh" , 200)

# std3 = std1 + std2
# print(std3)

# print(std1 > std2)
# print(std2 > std1)

# print(std1)

# P4 — Hard (Duck Typing)
# PDFReport, ExcelReport, WordReport classes banao. Har ek me generate() aur save() method. process_report(report) function banao jo koi bhi report le aur dono methods call kare. Teeno types se test karo.

class PDFReport:
    def generate(self):
        print("PDFRports generate ho raha he")

    def save(self):
        print("PDFRports save ho raha he")

class ExcelReport:
    def generate(self):
        print("ExcelRports generate ho raha he")

    def save(self):
        print("ExcelRports save ho raha he")

class WordReport:
    def generate(self):
        print("WordRports generate ho raha he")

    def save(self):
        print("WordRports save ho raha he")

def process_report(report):
    report.generate()
    report.save()

process_report(PDFReport())
process_report(ExcelReport())
process_report(WordReport())


# Email, SMS, Push (koi common parent nahi, duck typing)
# Sabme send(msg) → "Email: hello" jaisa return
# notify_all(channels, msg) function → loop me sab ka send call
# Bonus: naya WhatsApp class add karo, notify_all badle bina chale

class email:
    def send(self,msg):
        return f"email: {msg}"

class sms:
    def send(self,msg):
        return f"sms : {msg}"

class push:
    def send(self,msg):
        return f"push: {msg}"

class whatsapp:
    def send(self,msg):
        return f"whatsapp : {msg}"

def notify_all(channels,msg):
    for x in channels:
        print(x.send(msg))

notify_all([email(),sms(),push(),whatsapp()],"hello")

# add(*args) → kitne bhi numbers ka sum
class summer:
    def add(self,*args):
        return sum(args)
s = summer()
print(s.add(1,2,3))

# vector example
class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return vector(self.x + other.x , self.y + other.y)

    def __sub__(self,other):
        return vector(self.x - other.x , self.y - other.y)

    def __mul__(self,k):
        return vector(self.x * k , self.y * k)

    def __eq__(self,other):
        return (self.x,self.y) == (other.y,other.y)

    def __str__(self):
        return f"{self.x} , {self.y}"

    def __repr__(self):
        return f"{self.x} , {self.y}"

v1 = vector(10,20)
v2 = vector(5,4)
print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1 == vector(1, 2))   # True

# single dispatch
from functools import singledispatch

@singledispatch
def show(x):
    print("object :" , x)

@show.register(int)
def _(x):
    print("int value :" , x)

@show.register(str)
def _(x):
    print("string : " ,x)

@show.register(list)
def _(x):
    print("list :" ,x)

show(5)
show("kalpesh")
show([1,2,3])
show(2.5)  

# Project 1: Money

# __init__(amt)
# +, -, ==, <, __str__, __repr__
# Money + number aur number + Money dono chale

class money:
    def __init__(self,number,money):
        self.number = number
        self.money = money

    def __add__(self,other):
        return money(self.money + other.money, self.number + other.number)

    def __sub__(self,other):
        return money(self.money - other.money, self.number - other.number)

    def __str__(self):
        return f"{self.money} ,{self.number}"

    def __repr__(self):
        return f"{self.money} ,{self.number}"

m1 = money(10,20)
m2 = money(30,40)
print(m1 + m2)
print(m1 - m2)
print(10,20)
print(10,30)


# Project 3: Dispatch
# describe(x) singledispatch se: int, str, list, dict ke liye alag message

from functools import singledispatch

@singledispatch
def describe(x):
    print("object :" ,x)

@describe.register(int)
def _(x):
    print("int type value : ",x)

@describe.register(str)
def _(x):
    print("str type of string :",x)

@describe.register(list)
def _(x):
    print("list type of element :",x)

@describe.register(dict)
def _(x):
    print("dict type of value :",x)

describe(20)
describe("kalpesh")
describe([1,2,3,4,5])
describe({"name" : "kalpesh"})


