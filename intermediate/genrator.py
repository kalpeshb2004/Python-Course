# P1 — Easy
# EvenNumbers generator — start, end. Sirf even numbers yield kare. For loop se test karo.

def evenNumber(start,end):
    for i in range(start,end+1):
        if i % 2 == 0:
            yield i

for num in evenNumber(1,10):
    print(num)