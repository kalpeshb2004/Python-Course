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
