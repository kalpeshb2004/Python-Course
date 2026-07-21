# P1 — Easy
# Type hints ke saath functions banao:

# full_name(first: str, last: str) -> str
# is_adult(age: int) -> bool
# calculate_gpa(marks: list[float]) -> float

def full_name(first: str, last: str) -> str:
    return f"first: {first}, last: {last}"

print(full_name("kalpesh","bhure"))


def is_adult(age: int) -> bool:
    return age >= 18

print(is_adult(21))
print(is_adult(12))

def calculate_gpa(marks: list[float]) -> float:
    gpa = sum(marks) / len(marks)
    return f""

print(calculate_gpa([10,20,30.21,40]))

# P2 — Medium
# Student management functions — type hints ke saath:

# add_student(name: str, marks: dict[str, int]) -> None
# get_topper(students: list[dict]) -> str
# filter_passed(students: list[dict], passing: int) -> list[dict]

students = [
    {"name" : "kalpesh" , "marks" : {"math" : 95, "science" : 87}},
    {"name" : "jayesh" , "marks" : {"math" : 90, "science" : 57}},
    {"name" : "rahul" , "marks" : {"math" : 65, "science" : 77}},
    {"name" : "ram" , "marks" : {"math" : 67, "science" : 97}}
]

def add_student(name: str, marks: dict[str, int]) -> None:
    students.append({"name" : name, "marks" : marks})
    print(f"student: {name} added")


def get_topper(students: list[dict]) -> str:
    topper = max(students,key=lambda s: sum(s["marks"].values()))
    return topper["marks"]

def filter_passed(students: list[dict], passing: int) -> list[dict]:
    return [s for s in students if all(m >= passing for m in s["marks"].values())]

add_student("Raj", {"maths": 99, "science": 98})
print(get_topper(students))
print(filter_passed(students,60))







