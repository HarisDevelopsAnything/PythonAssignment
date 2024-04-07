import math
def findnth(n):
    if(n%2==0):
        a=1
        r= 3
        n=n//2
        return (int(a*(r**(n-1))))
    else:
        a=1
        r= 2
        n=int(math.ceil(n/2))
        return (int(a*(r**(n-1))))