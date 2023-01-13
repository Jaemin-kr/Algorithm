import sys

a = list(map(int, sys.stdin.readline().split()))
dif = a[1]-a[0]
print(dif-1)

for i in range(dif):
    print(i+a[0],end=' ')