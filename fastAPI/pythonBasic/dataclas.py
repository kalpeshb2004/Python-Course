# Class banate waqt normal tarike se __init__, __repr__ sab manually likhna padta he. Dataclass ye sab auto-generate kar deta.

# normal data class 
class student:
    def __init__(self,name: str,age: int):
        self.name = name
        self.age = age
    
    def __repr__(self):
         return f"name: {self.name} , age: {self.age}"

s1 = student("kalpesh" , 21)
# print(s1)

from dataclasses import dataclass
@dataclass
class student:
    name: str
    age: int

s1 = student("kalpesh bhure" , 22)
print(s1)

# P1 — Easy
# Dataclass bana Book:
# title: str
# author: str
# price: float = 0.0 (default)

from dataclasses import dataclass

@dataclass
class esy():
    title: str
    author: str
    price: float = 0.0

e1 = esy("jungle book" , "shecksphere")
print(e1)

# P2 — Medium
# Dataclass bana Product:

# name: str
# price: float
# quantity: int

# Function likh total_cost(product: Product) -> float jo price * quantity return kare. 2-3 products bana ke total cost print kar.

from dataclasses import dataclass

@dataclass
class book():
    name: str
    price: float
    quantity: int

def total_cost(product: book) -> float:
    return product.price * product.quantity

p1 = book("Laptop", 50000.0, 2)
p2 = book("Mouse", 500.0, 3)
p3 = book("Keyboard", 1200.0, 1)

print(f"{p1.name}: {total_cost(p1)}")
print(f"{p2.name}: {total_cost(p2)}")
print(f"{p3.name}: {total_cost(p3)}")

