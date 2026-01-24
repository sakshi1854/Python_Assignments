# Design a python application that creates two threads.
# Thread 1 should compute sum of elements from a list 
# Thread 2 should compute product of elements from a list.
# Return the result to the main thread and display them.


import threading
import time

sum_result=0
product_result=1

def SumResult(No):
    global sum_result
    size=len(No)
    for i in range(size):
        sum_result=sum_result+No[i]

def ProductResult(No):
    size=len(No)
    global product_result
    for i in range(size):
        product_result=product_result*No[i]


def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    global sum_result
    global product_result
    start_time=time.time()
    t1=threading.Thread(target=SumResult,args=(Data,))
    t2=threading.Thread(target=ProductResult,args=(Data,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time=time.time()
    print("The execution time is:",end_time-start_time)
    print("The sum of elements from list is:",sum_result)
    print("The produce of elements from list is:",product_result)
    print("Exit from main")

if __name__=="__main__":
    main()