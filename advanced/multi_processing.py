# Easy: Ek function banao jo apna naam print kare, use ek Process me run karo (start + join ke sath).

import multiprocessing
import time

def task(name):
    print(f"{name} call kiya")
    time.sleep(2)
    print(f"{name} call done")
    

if __name__ == "__main__": 
    t1 = multiprocessing.Process(target=task,args=("procces-1",))
    t2 = multiprocessing.Process(target=task,args=("procces-2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


