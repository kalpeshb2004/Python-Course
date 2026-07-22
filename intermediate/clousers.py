# P1 — Easy (Closure)
# counter() closure banao — har call pe count badhaye.
# pythonc = counter()
# c()   # → Count: 1
# c()   # → Count: 2
# c()   # → Count: 3

def counter(count):
    def inner():
        nonlocal count #nonlocal variable ko modify karne ke liye use kiya jata , access deta he modify karne ka 
        count += 1
        print(count)
    return inner

c = counter(0)
c()
c()
c()


