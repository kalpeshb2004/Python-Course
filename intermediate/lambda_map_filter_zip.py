# Q1 — LAMBDA
# Lambda function banao jo number ka cube return kare.
# cube(3) → 27
# cube(4) → 64

# cube = lambda a: a**3
# print(cube(3))

# cube = lambda a: a**3
# print(cube(4))

# Q2 — MAP
# Names list lo — har naam ke saath "Hello" add karo map se.
# ["Raj", "Jay"] → ["Hello Raj", "Hello Jay"]

# lst = ["Raj","Jay"]
# hlo = list(map(lambda x: "hello " + x , lst))
# print(hlo)

# Q3 — FILTER
# Numbers list lo — sirf 50 se zyada wale filter karo.
# [23, 67, 45, 89, 12, 56] → [67, 89, 56]

# nums = [23, 67, 45, 89, 12, 56]
# fltr = list(filter(lambda x: x > 50,nums))
# print(fltr)

# Q4 — ZIP
# 2 lists lo — subjects aur marks. Zip karo aur print karo.
# ["Maths", "Science"] + [95, 88] → Maths: 95, Science: 88

sub = ["Maths", "Science"]
marks = [95, 88]

for sub,marks in zip(sub,marks):
    print(f'{sub} : {marks}')


