from dataclasses import dataclass

@dataclass
class student:
    name: str
    age: int

s1 = student("kalpesh bhure" , 22)
print(s1)