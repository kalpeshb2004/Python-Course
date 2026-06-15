

# # P1 — printer queue
# # pythondocuments = ["doc1", "doc2", "doc3", "doc4", "doc5"]
# # queue banao → ek ek print karo → print hone pe print karo:
# #using collection

# from collections import deque 

# docs = deque(["doc1", "doc2", "doc3", "doc4", "doc5"])

# while docs:
#     new_deque = docs.popleft()
#     print("printing: " , new_deque)

# # isme collections ,dequeue creation, popleft sb use horaha he 

# P2 — hot potato game
# pythonplayers = ["ram", "sam", "tom", "jay", "roy"]

# queue me daalo
# N baar rotate karo (front se uthao → back me daalo)
# N baar baad jo front pe hai → OUT!
# ek bachega → winner!

# N = 3
# out: tom
# out: ram
# out: jay
# out: roy
# winner: sam

# from collections import deque
# layers = deque(["ram", "sam", "tom", "jay", "roy"])
# n = 3
# while len(layers) > 1:
#     for i in range(n-1):
#       new_layers = layers.popleft()
#       layers.append(new_layers)
#     layers.popleft()
# print(layers[0])

# P3 — recent items tracker
# maxlen use karke last 3 visited pages track karo:
# visit("google.com")
# visit("youtube.com")
# visit("github.com")
# visit("stackoverflow.com")
# # google.com auto remove!
# print(history)
# # deque(['youtube.com', 'github.com', 'stackoverflow.com'], maxlen=3)
# function use hoga 
# from collections import deque

# deque1 = deque(maxlen=3)

# def visit(url):
#     deque1.append(url)

# def current():
#     if len(deque1) > 0:
#        print(deque1)

# visit("google.com")
# visit("youtube.com")
# visit("github.com")
# visit("stackoverflow.com")
# current()