# Easy: Ek function banao jo apna naam print kare, use ek Process me run karo (start + join ke sath).

# import multiprocessing
# import time

# def task(name):
#     print(f"{name} call kiya")
#     time.sleep(2)
#     print(f"{name} call done")
    

# if __name__ == "__main__": 
#     t1 = multiprocessing.Process(target=task,args=("procces-1",))
#     t2 = multiprocessing.Process(target=task,args=("procces-2",))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

# Medium: 3 processes banao jo har ek alag number ka square calculate karke print kare (args use karke number pass karo).

# import multiprocessing
# import time

# def task(num):
#     print(f"{num*num}")

# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=task,args=(10,))
#     p2 = multiprocessing.Process(target=task,args=(20,))
#     p3 = multiprocessing.Process(target=task,args=(30,))

#     p1.start()
#     p2.start()
#     p3.start()

#     p1.join()
#     p2.join()
#     p3.join()
    
# Hard: Manager().list() use karke 5 processes banao jo apna result (jaise process_id * 10) shared list me append karein, fir main process me print karo.
    
import multiprocessing
import time



def task(pid,shared_list):
    shared_list.append(pid*10)
    
if __name__ == "__main__":
    manager = multiprocessing.Manager()
    shared_list = manager.list()


    processes = []

    for i in range(1,6):
        p = multiprocessing.Process(target=task,args=(i,shared_list))
        processes.append(p)
        p.start()


    for p in processes:
        p.join()

    print(list(shared_list))

    


