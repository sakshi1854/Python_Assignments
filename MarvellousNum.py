def ChkPrime(No1):
    isPrime=True
    if No1<=1:
        return False
    else:
        for i in range(2,No1//2+1):
            if No1%i==0:
                isPrime=False
                break
        return isPrime
    