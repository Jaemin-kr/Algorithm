import sys

arr = []
for i in range(7):
    a = int(sys.stdin.readline())
    if a % 2 != 0: arr.append(a)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)