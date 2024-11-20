def isPrime(n):
    for it in range(2,n):
      if(n%it==0):
         return False
    return True


def primeNum(number):
    for it in range(0,number):
        if(isPrime(it)):
         print(it)
        
primeNum(50)