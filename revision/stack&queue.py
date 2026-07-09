# STACK & QUEUE
# Q1 — Easy (Stack)
# Stack use karo — string lo, reverse karo using stack. pop() se nikalo.

from collections import deque

stack = deque("kalpesh")
# word = "kalpesh"

# for char in word:
#     stack.append(char)

result = ""
while stack:
    result = result + stack.pop()

print(result)


# Q2 — Medium (Queue)
# Queue use karo — 5 customers add karo. Ek ek karke serve karo aur print karo "Serving: name".




