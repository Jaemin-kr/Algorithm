import sys

a = int(input())
arr = [0] * 10001 #리스트 초기화, append사용시 메모리 초과

for i in range(a):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)

#리스트 한줄씩 출력
#print(*arr, sep='\n')