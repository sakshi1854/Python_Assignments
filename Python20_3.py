# Design a python application that creates two threads names EvenList and OddList.
# Both threads should accept a list of integers as input.
# The EvenList thread should: Extract all even elements from the list.
# Calculate and display their sum.
# The oddlist thread should extract all odd elements from the list.
# Calculate and display their sum
# Threads should run concurrently.

import threading
import time

def EvenList(Data):
    size=len(Data)
    sum=0
    for i in range(size):
        if Data[i]%2==0:
            print(Data[i],end=" ")
            sum=sum+Data[i]
    print()
    print("The sum of even elements from list is:",sum)

def OddList(Data):
    size=len(Data)
    sum=0
    for i in range(size):
        if Data[i]%2!=0:
            print(Data[i],end=" ")
            sum=sum+Data[i]
    print()
    print("The sum of odd elements from the list is:",sum)

def main():
    start_time=time.time()
    lst=[1,2,3,4,5,6,7,8,9,10]
    t1=threading.Thread(target=EvenList,args=(lst,))
    t2=threading.Thread(target=OddList,args=(lst,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time=time.time()
    print("The execution time is:",end_time-start_time)
    print("Exit from main function")

if __name__=="__main__":
    main()