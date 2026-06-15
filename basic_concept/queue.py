# P1 — printer queue
# pythondocuments = ["doc1", "doc2", "doc3", "doc4", "doc5"]
# queue banao → ek ek print karo → print hone pe print karo:
#using collection

from collections import deque 

docs = deque(["doc1", "doc2", "doc3", "doc4", "doc5"])

while docs:
    new_deque = docs.popleft()
    print("printing: " , new_deque)

# isme collections ,dequeue creation, popleft sb use horaha he 

