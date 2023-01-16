import sys
arr = []

for i in range(9):
    arr.append(int(sys.stdin.readline()))

total = sum(arr)
a, b = 0, 0

for i in range(9):
    for j in range(i+1, 9):
        if total - (arr[i]+arr[j]) == 100:
            a,b = arr[i], arr[j]
            break

arr.remove(a)
arr.remove(b)
arr.sort()

for i in arr:
    print(i)