import sys

a,b = map(int, sys.stdin.readline().split())
a1 = min(a,b)
b1 = max(a,b)

dif = b1-a1-1

if a1 == b1 or a1+1 == b1:
    dif = 0
print(dif)

for i in range(a1+1,b1):
    print(i, end=' ')