# Design a python application that creates two threads named as Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that: Thread2 starts execution only after thread1 has completed.
# Use appropriate thread synchronization.

import threading
import time

def Display():
    for i in range(1,51):
        print(i,end=" ")
    print()

def DisplayReverse():
    for i in range(50,0,-1):
        print(i,end=" ")
    print()

def main():
    start_time=time.time()
    t1=threading.Thread(target=Display)
    t2=threading.Thread(target=DisplayReverse)
    print("Thread1 is starting.....")
    t1.start()
    t1.join()
    print("Thread1 completed successfully...")
    print("Thread2 is starting....")
    t2.start()
    t2.join()
    print("Thread2 is completely successfully....")
    end_time=time.time()
    print("The execution time is:",end_time-start_time)


if __name__=="__main__":
    main()