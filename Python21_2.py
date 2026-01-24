# Design a python application that creates two threads.
# Thread1 should calculate and display the maximum element from an list.
# Thread2 should calculate and display the minimum element from the same list.
#The list should be accepted from user.


import threading
import time

def Maximum(No):
    size=len(No)
    maximum=No[0]
    for i in range(size):
        if No[i]>maximum:
            maximum=No[i]
    print("The maximum element from list is:",maximum)

def Minimum(No):
    size=len(No)
    minimum=No[0]
    for i in range(size):
        if No[i]<minimum:
            minimum=No[i]
    print("The minimum element from list is:",minimum)

def main():
    Data=list()
    size=int(input("Enter the number of elements:"))
    for i in range(size):
        Ret=int(input())
        Data.append(Ret)
    print("The original elements are:",Data)
    start_time=time.time()
    t1=threading.Thread(target=Maximum,args=(Data,))
    t2=threading.Thread(target=Minimum,args=(Data,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time=time.time()
    print("The execution time is:",end_time-start_time)
    print("Exit from main")


if __name__=="__main__":
    main()