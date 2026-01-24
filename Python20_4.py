# Design a python application that creates three threads named as Small,Capital,and Digits.
# All threads should accept the string as input.
# The small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display : ThreadID,ThreadName


import threading
import time

def SmallCase(data):
    count=0
    for ch in data:
        if ch.islower():
            print(ch,end=" ")
            count=count+1
    print()
    print("The number of small case characters is:",count)
    print("The ThreadId for given thread is:",threading.get_ident())
    print("The Thread Name is:",threading.current_thread().name)

def UpperCase(data):
    count=0
    for ch in data:
        if ch.isupper():
            print(ch,end=" ")
            count=count+1
    print()
    print("The number of upper case characters is:",count)
    print("The ThreadID for given thread is:",threading.get_ident())
    print("The threading name for given thread is:",threading.current_thread().name)

def DigitCase(data):
    count=0
    for ch in data:
        if ch.isdigit():
            print(ch,end=" ")
            count=count+1
    print()
    print("The number of digits is:",count)
    print("The thread id for the given thread is:",threading.get_ident())
    print("The thread name for given thread is:",threading.current_thread().name)


def main():
    data="Sakshi Rajpal Choudhari 18052004"
    start_time=time.time()
    t1=threading.Thread(target=SmallCase,args=(data,))
    t2=threading.Thread(target=UpperCase,args=(data,))
    t3=threading.Thread(target=DigitCase,args=(data,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    end_time=time.time()
    print("The execution time is:",end_time-start_time)
    print("Exit from main")

if __name__=="__main__":
    main()