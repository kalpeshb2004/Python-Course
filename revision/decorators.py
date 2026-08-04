# def log(level):
#     def decorator(func):
#         def wrapper(*args, **kwarsgs):
#             print(f"{level} start")
#             result = func(*args, **kwarsgs)
#             print(f"{level} end")
#             return result
#         return wrapper
#     return decorator

# @log("INFO")
# def process():
#     print("proccessing.....")

# process()

# P2 — Medium
# @validate_age(min_age, max_age) decorator banao — age range validate kare.

# def validate_age(min_age, max_age): #outer funcion sirf argument leta
#     def decorator(func):# ye niche wale register func ko store karata
#         def wrapper(name,age):# ye user argument leta he 
#             if min_age <= age <= max_age:
#                 return func(name, age) # register func return karata
#             else:
#                 print(f"Age must be {min_age}-{max_age}")
#         return wrapper
#     return decorator


# @validate_age(18,60)
# def register(name,age):
#     print(f"{name} registered")

# register("kalpesh" , 21)
# register("Ram", 15)

# def uppercase(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# @uppercase
# def greet():
#     return "hello world"

# print(greet())  # → HELLO WORLD

# P2
# @timer decorator — function kitne time me chala print kare.



# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{result},{end - start : .2f} sec")
#         return result
#     return wrapper

# @timer
# def slow():
#     time.sleep(1)
#     return "done"

# slow()  # → done, Time: 1.00 sec

# P3
# @repeat(n) — function n baar chalaye.

# python
# @repeat(3)
# def hello():
#     print("Hello!")

# def repeat(n):
#   def decorator(func):
#     def wrapper(*args , **kwargs):
#         for i in range(n):
#             func()
#     return wrapper
#   return decorator

# @repeat(3)
# def hello():
#     print("Hello!")

# hello()

# P1 — Medium
# @retry(times) decorator — function fail ho toh times baar retry kare.

# python
# @retry(3)
# def unstable():
#     import random
#     if random.random() < 0.7:  # 70% chance fail
#         raise Exception("Failed!")
#     print("Success!")

# unstable()
# # → Attempt 1 failed, retrying...
# # → Attempt 2 failed, retrying...
# # → Success!


# def retry(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f"Attempt {i+1} failed, retrying...")
#                 print("all exception failed")
#         return wrapper
#     return decorator

# @retry(3)
# def unstable():
#     import random
#     if random.random() < 0.7:
#         raise Exception("failed")
#     print("success")

# unstable()

# P2 — Medium
# @cache decorator — same arguments dobara aaye toh calculate mat karo — store se return karo.

# python
# @cache
# def square(n):
#     print(f"Calculating {n}²")
#     return n * n

# square(5)   # → Calculating 25
# square(5)   # → 25 (cache se — print nahi)
# square(3)   # → Calculating 9


def cache(func):
    cache_store = {}
    def wrapper(*args):
        if args in cache_store:
            return cache_store[args]
        result = func(*args)
        cache_store[args] = result
        return result
    return wrapper

@cache
def square(n):
    print(f"Calculating {n*n}")
    return n * n

square(5)   # → Calculating 25
square(5)   # → 25 (cache se — print nahi)
square(3)   # → Calculating 9
