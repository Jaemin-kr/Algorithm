import sys
a, b, c = map(int, sys.stdin.readline().split())

cnt = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print("%d %d %d" %(i,j,k))
            cnt = cnt+1
print(cnt)
