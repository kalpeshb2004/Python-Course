# P1 — Easy
# Person class banao with parameterized constructor — name, city. Method greet() → "Namaste, mera naam Raj hai aur me Mumbai se hu"

# class person:
#     def __init__(self,name,city):
#         self.name = name
#         self.city = city
    
#     def greet(self):
#         print(f'Namaste, mera naam {self.name} he aur me {self.city} se hu')
    
# per = person("raj","Mumbai")
# per.greet()

# P2 — Easy-Medium
# Product class banao with default value constructor — name, price=0, discount=0. Method final_price() → price - discount print karo.

# class Product:
#     def __init__(self,name,price=0,discount=0):
#         self.name = name
#         self.price = price
#         self.discount = discount

#     def final_price(self):
#         print(f'name: {self.name} , price: {self.price} discount: {self.discount}%')

# prdt = Product("kalpesh" ,100,10)

# prdt.final_price()
        

# P3 — Medium
# Circle class banao — radius parameter. Constructor me hi calculate karo:
# self.area = π × r²
# self.circumference = 2 × π × r

# class circle:
#     def __init__(self):
#         self.radius = 3.14 * (10 * 10)
#         self.parameter = 2 * 3.14 * 10

# crl = circle()
# print(crl.radius)
# print(crl.parameter)

# P4 — Hard

# Employee class banao — name, salary, department. Default department = "General". Constructor me:
# Agar salary < 0 → "Invalid salary" print karo aur self.salary = 0 set karo
# self.annual_salary = salary × 12 calculate karo
# Method: show_details() → sab info print karo.

class employee:
    def __init__(self,name,salary,department="General"):
        self.name = name
        self.salary = salary
        self.department = department
        
        if salary < 0:
            print("Invalid salary")
            self.salary = 0
        else:
            self.salary = salary

            self.annual_salary = salary * 12

    def show_details(self):
        print(f' name: {self.name}\n salary: {self.salary}\n department: {self.department}\n annual_salary: {self.annual_salary}')

emp = employee("kalpesh" ,100000)
emp.show_details()
   
        
    


