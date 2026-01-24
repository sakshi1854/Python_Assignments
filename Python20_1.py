# 1. Write a python application that creates two separate threads named as Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import threading
import time

def DisplayEven():
    for i in range(1,11):
        print(i*2,end=" ")
    print()

def DisplayOdd():
    for i in range(1,20,2):
        print(i,end=" ")
    print()

def main():
    start_time=time.time()
    t1=threading.Thread(target=DisplayEven)
    t2=threading.Thread(target=DisplayOdd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end_time=time.time()
    print("The execution time is:",end_time-start_time)

if __name__=="__main__":
    main()