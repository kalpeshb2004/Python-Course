class A:
    def __init__(self, v): self.v = v
    def __add__(self, o): return A(self.v + o.v)
    def __repr__(self): return f"A({self.v})"
print(A(1) + A(2))
print(A(1) + 5)