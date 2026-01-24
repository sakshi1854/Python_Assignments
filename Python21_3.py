# Display a python application where multiple threads update a shared variable.
# Use a Lock to avoid race condition.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.


import threading
import time

iCnt=0

lobj=threading.Lock()

def Increment():
    global iCnt
    for i in range(200000):
        with lobj:
            iCnt=iCnt+1
def main():
    global iCnt
    start_time=time.time()
    t1=threading.Thread(target=Increment)
    t2=threading.Thread(target=Increment)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time=time.time()
    print("The execution time is:",end_time-start_time)
    print("The value of iCnt is:",iCnt)
    print("Exit from main")


if __name__=="__main__":
    main()
