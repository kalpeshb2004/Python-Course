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

