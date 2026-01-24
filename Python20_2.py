# 2.Design a python application that creates two threads named as EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter.
# The EvenFactor thread should: Identify all even factors of given number.
# Calculate and display the sum of even factors.
# The OddFactor thread should: Identify all odd factors of given number.
# Calculate and display the sum of odd factors.
# After both threads complete execution,the main thread should display the message: "Exit from main."

import threading
import time

def SumEven(No):
    sum=0
    for i in range(1,No+1):
        if No%i==0 and i%2==0:
            print(i,end=" ")
            sum=sum+i
    print()
    print("The sum of even factors is:",sum)

def SumOdd(No):
    sum=0
    for i in range(1,No+1):
        if No%i==0 and i%2!=0:
            print(i,end=" ")
            sum=sum+i
    print()
    print("The sum of odd factors is:",sum)

def main():

    start_time=time.time()
    t1=threading.Thread(target=SumEven,args=(1000,))
    t2=threading.Thread(target=SumOdd,args=(1000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time=time.time()
    print("The execution time is:",end_time-start_time)
    print("Exit from main")

if __name__=="__main__":
    main()