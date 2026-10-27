# P1 — Easy (Single)
# Vehicle class banao — brand, speed. Method show(). Car class banao jo inherit kare — extra attribute doors. Car ka object banao aur show karo.
#using super keywords and constructor 

# class vehicle:
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed
    
#     def show(self):
#         print(f"brand: {self.brand} , speed: {self.speed}")

# class car(vehicle):
#     def __init__(self, brand, speed,doors):
#       super().__init__(brand, speed)
#       self.doors = doors
    
#     def show1(self):
#         print(f'doors: {self.doors}')

# c1 = car("farari",300,"upwords")
# c1.show()
# c1.show1()


    
# P2 — Medium (Multilevel)
# Person → Employee → Manager chain banao.
# Person: name, age
# Employee: company, salary
# Manager: team_size
# Har level me introduce() method — super() use karke upar ka bhi print karo.

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f'name: {self.name} , age: {self.age}') 
       
# class employee(person):
#     def __init__(self, name, age,company,salary):
#         super().__init__(name, age)
#         self.company = company
#         self.salary  = salary
    
#     def introduce(self):
#         super().introduce()
#         print(f'company: {self.company} , salary: {self.salary}') 

# class manager(employee):
#     def __init__(self, name, age, company, salary,team_size):
#         super().__init__(name, age, company, salary)
#         self.team_size = team_size

#     def introduce(self):
#         super().introduce()
#         print(f'team size: {self.team_size}')

# m1 = manager("kalpesh",21,"RBIs",100000,30)
# m1.introduce()


# P3 — Medium (Multiple)
# Flyable class — method fly(). Swimmable class — method swim(). Duck class dono se inherit kare + apna quack(). Duck object se teeno methods bulao.

# class flyable:
#     def fly(self):
#         print("birds fly")
        
# class swimmable:
#     def swim(self):
#         print("fishes swim")

# class duck(flyable,swimmable):
#     def quack(self):
#         print("duck fly and swim")

# d1 = duck()
# d1.fly()
# d1.swim()
# d1.quack()

# P4 — Hard (Hierarchical + super)
# Shape class — color, method draw(). 3 child classes: Circle(radius), Rectangle(length, width), Triangle(base, height). Har child me:
# super().__init__(color) use karo
# area() method
# draw() override karo — "Drawing [color] circle" etc.

# Shape
# ├── Circle   → area = πr²
# ├── Rectangle → area = l×w
# └── Triangle  → area = ½×b×h

#Hierarchical = ek baap kai bete

# class shape:
#     def __init__(self,color):
#         self.color = color

#     def draw(self):
#         print("drawing with color")

#     def area(self):
#         print("parent shape area\n")
    
    
# class circle(shape):
#     def __init__(self, color,radius):
#         super().__init__(color)
#         self.radius = radius
    
#     def area(self):
#         super().area()
#         print(f'area of circle: {3.14 * self.radius * self.radius}')
    
#     def draw(self):
#         super().draw()
#         print(f'drawing {self.color} circle\n')
    

# class rectangle(shape):
#     def __init__(self, color,length,width):
#         super().__init__(color)
#         self.length = length
#         self.width = width
    
#     def area(self):
#         super().area()
#         print(f'area of ractangle: {self.length * self.width}')
    
#     def draw(self):
#         super().draw()
#         print(f'drawing {self.color} rectangle\n')

# class traingle(shape):
#     def __init__(self, color,base,height):
#         super().__init__(color)
#         self.base = base
#         self.height = height
    
#     def area(self):
#         super().area()
#         print(f'area of traingle: {(1/2) * self.base * self.height}')

#     def draw(self):
#         super().draw()
#         print(f'drawing {self.color} traingle')

# crl = circle("red" , 10); crl.area(); crl.draw()
# rect = rectangle("white",10,20); rect.area(); rect.draw()
# tri = traingle("bhagwa",10,20); tri.area(); tri.draw() 


# ✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️
# Project: Vehicle chain

# Vehicle(brand, speed) → info()
# Car(Vehicle) → extra doors, info() override with super()
# ElectricCar(Car) → extra battery (multilevel)
# Bike(Vehicle) → extra has_gear (hierarchical)
# Sab ka info() loop me call.

class vehicle:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name

    def info(self):
        return f"{self.brand} is real {self.name}"

class car(vehicle):
    def __init__(self,brand,name,doors):
        super().__init__(brand,name)
        self.doors = doors

    def info(self):
        return f"{self.brand} is real {self.name} ha {self.doors}"

class electricCar(car):
    def __init__(self,brand,name,doors,battery):
            super().__init__(brand,name,doors)
            self.battery = battery

    def info(self):
        return f"{self.brand} is real {self.name} ha {self.battery}"

class bike(vehicle):
     def __init__(self,brand,name,has_gear):
        super().__init__(brand,name)
        self.has_gear = has_gear

     def info(self):                                  # override
        return super().info() + f", gear={self.has_gear}"

vehicles = [
    car("Suzuki", "Swift", 4),
    electricCar("Tata", "Nexon EV", 4, 40),
    bike("Yamaha", "R15", True),
]
for v in vehicles:
    print(v.info())


# Pillar 3: Inheritance (Part 2)
# Aaj: multiple, hybrid, MRO, diamond, super() deep, mixin.

class parent:
    def hi(self): return "parent"

class mother:
    def by(self): return "mother"

class child(parent,mother):
    pass

c = child()
print(c.hi(),c.by())

# multilevel + multiple + with __mro__ 
class father:
    def hi(self): print("father")

class mother1(father):
    def hi(self): print("mother1"); super().hi()

class mother2(father):
    def hi(self): print("mother2"); super().hi()

class child(mother1,mother2):
    def hi(self): print("mother1,mother2"); super().hi()

child().hi()
print(child.__mro__)

# agar multiple me mro hua to super() lagega aur 
# pehele child mother1,mother2 then father print hoga 

# __init__ + multiple 
class a:
    def __init__(self):
        print("a")

class b(a):
    def __init__(self):
        print("b")
        super().__init__()

class c(a):
    def __init__(self):
        print("c")
        super().__init__()

class d(b,c):
    def __init__(self):
        print("d")
        super().__init__()

d()

# Project 1: Diamond
# A → B, C → D banao. Har class hi() me naam print + super().hi(). Output predict kar, phir

class a:
    def hi(self): print("a")

class b(a):
    def hi(self): print("b"); super().hi()

class c(a):
    def hi(self): print("c"); super().hi()

class d(b,c):
    def hi(self): print("d"); super().hi()

d()

# Person(name) → Student(Person) (roll) + Employee(Person) (salary) → Intern(Student, Employee). info() me sab dikhe. __mro__ print kar.

class person:
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name = name

    def info(self):
        return f"name is {self.name}"

class student(person):
    def __init__(self,roll,**kwargs):
        super().__init__(**kwargs)
        self.roll = roll

    def info(self):
        return f"roll is {self.roll} , " + super().info()

class employee(person):
    def __init__(self,salary,**kwargs):
        super().__init__(**kwargs)
        self.salary = salary

    def info(self):
        return f"salary is {self.salary} , " + super().info()

class intern(student,employee):
    pass

i = intern(name="kalpesh" ,roll= 6, salary = 10000)
print(i.info())
print(intern.__mro__)





