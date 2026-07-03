# P1 — Easy
# EvenNumbers iterator class banao — start, end. Sirf even numbers yield kare. For loop se test karo
# its difficut one 

class evenNumber():
    def __init__(self,start,end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current < self.end:
            if self.current % 2 == 0:
                value = self.current
                self.current += 1
                return value
            self.current += 1
        raise StopIteration

e = evenNumber(1,10+1)
for num in e:
    print(num)
