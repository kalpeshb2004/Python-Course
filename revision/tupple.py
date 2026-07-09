# TUPLE
# Q1 — Easy
# Student ka data tuple me store karo (name, age, marks). Unpack karo aur print karo.

# data = (("kalpesh",21,72),
#                     ("jayesh",25,68),
#                     ("ram",36,100))
# for name,age,marks in data:
#     print(name)

# Q2 — Medium
# List of tuples lo [(name, marks)] — marks ke basis pe sort karo. sorted() + lambda use karo.


data = [("kalpesh",21,72),
                    ("jayesh",25,68),
                    ("ram",36,100)]

soerted_data = sorted(data ,key=lambda x: x[2])
print(soerted_data)
    