# Closures

# A closure is an inner function that remembers variables from the outer function, even after the outer function has finished.

def make_multiplier(n):
    def multiply(x):
        return x * n      # 'n' is remembered from the outer scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15


# P2 — Easy-Medium (Decorator)
# uppercase decorator banao — function ka string output uppercase kare.
# python@uppercase
# def greet(name):
#     return f"hello {name}"

# print(greet("kalpesh"))   # → HELLO KALPESH

def uppercase(func):
    def wrapper(*args,**kwargs):
        print("pehele")
        new_str = func(*args,**kwargs)
        print("baad me")
        return new_str.upper()
    return wrapper

@uppercase
def greet(name):
    return name

print(greet("kalpesh"))


def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print("Done")
        return result
    return wrapper

@log_call
def greet(name):
    print(f"Hello, {name}!")

greet("Asha")
# Calling greet
# Hello, Asha!
# Done

# Generators

# A generator produces values one at a time, on demand, using yield. It pauses after each yield and resumes where it left off, so it doesn’t hold everything in memory.

def count_up(limit):
    i = 1
    while i <= limit:
        yield i
        i += 1

for num in count_up(3):
    print(num)

# 1
# 2
# 3

# function baar baar call nahi hoga just yeild resume aur pause hoga har value returning pe