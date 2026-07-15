#basic program of multithreading 
# import threading
# import time

# def task(name):
#     print(f"{name} start")
#     time.sleep(2)
#     print(f"{name} done")

# t1 = threading.Thread(target=task, args=("thread-1",))
# t2 = threading.Thread(target=task, args=("thread-2",))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("all task finished")

# Easy:
# Ek function likho jo "Hello" print kare, use ek thread me run karo aur start() + join() use karo.

# import threading

# def hel(name):
#     print(f"{name}")

# t1 = threading.Thread(target=hel, args=("Hello",))

# t1.start()
# t1.join()

# print("hello high hogaya")

# Easy-Medium:
# 2 threads banao jo alag-alag numbers (1 se 5) print karein counter ke sath, dono ko sequentially start aur join karo.

# import threading

# def task(name):
#     for i in range(1,6):
#         print(f"{name}: {i}")

# t1 = threading.Thread(target=task, args=("thread-1",))
# t2 = threading.Thread(target=task, args=("thread-2",))

# t1.start()
# t1.join()
# t2.start()
# t2.join()

# print("he he")

# Medium:
# Ek shared variable counter = 0 hai. 2 threads ise 100000 baar increment karte hain bina Lock use kiye — output kya galat aayega? Fir Lock use karke fix karo.

import threading

counter = 0
lock = threading.Lock() # lock object banaya

def task():
    global counter
    for i in range(100000):
        lock.acquire()
        #with lock: ye automatically acquire and release karega 
        counter+=1
        lock.release()
        
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
t1.join()
t2.join()

print(counter)









