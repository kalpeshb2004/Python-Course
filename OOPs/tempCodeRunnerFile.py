
# class Person:
#     count = 0

#     def __init__(self, name, age):
#         self.name, self.age = name, age
#         Person.count += 1

#     def greet(self):                        # instance
#         return f"Hi {self.name}"

#     @classmethod
#     def from_string(cls, s):                # alt constructor
#         name, age = s.split("-")
#         return cls(name, int(age))

#     @staticmethod
#     def is_adult(age):                      # utility
#         return age >= 18

# p = Person.from_string("Raj-25")
# print(p.greet(), Person.is_adult(p.age), Person.count)