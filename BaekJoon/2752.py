import sys

a = list(map(int,sys.stdin.readline().split()))
a.sort()
print(a[0],a[1],a[2])