import sys

a, b, c = list(map(int,sys.stdin.readline().split()))

def POW(a,n):
    if n==1: 
        return a % c
    else:
        val = POW(a, n//2)
        if n%2 == 0: 
            return (val*val)%c
        else:
            return val * val * a % c
print(POW(a,b))
