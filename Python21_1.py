# Design a python application that creates two threads named prime and nonprime.
# Both threads should accept a list of integers.
# The prime thread should display all prime numbers from list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading
import time

def ChkPrime(No):
    if No<=1:
        return False
    for i in range(2,No//2+1):
        if No%i==0:
            return False
    return True

def Prime(No):
    DataPrime=list()
    size=len(No)
    for i in range(size):
        if(ChkPrime(No[i])):
            DataPrime.append(No[i])
    print("The Prime numbers are:")
    print(DataPrime)

def NonPrime(No):
    DataNonPrime=list()
    size=len(No)
    for i in range(size):
        if(not ChkPrime(No[i])):
            DataNonPrime.append(No[i])
    print("The non-prime numbers are:")
    print(DataNonPrime)
        
def main():
    Data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    start_time=time.time()
    t1=threading.Thread(target=Prime,args=(Data,))
    t2=threading.Thread(target=NonPrime,args=(Data,))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    end_time=time.time()
    print("The execution time is:",end_time-start_time)
    print("Exit from main")

if __name__=="__main__":
    main()