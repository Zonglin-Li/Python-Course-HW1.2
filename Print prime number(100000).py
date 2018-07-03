#Prime number

from math import sqrt
def PrimeNumber(n):
    for i in range(2,n):
        flg=True
        for j in range(2, int(sqrt(i))+1):          #试除法
            if(i%j == 0):
                flg=False
        if(flg==True):
            print(i)

PrimeNumber(100000)
