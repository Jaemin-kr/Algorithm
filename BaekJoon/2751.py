import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)

arr = sorted(arr)
for i in range(n):
    print(arr[i])