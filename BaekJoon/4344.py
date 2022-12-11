T = int(input())
avg = 0
total = 0
cnt = 0
ans = 0
for i in range(T):
    arr = list(map(int, input().split()))
    #print(arr[0])
    for i in range(1,arr[0]+1):
        total += arr[i]
        avg = total/arr[0]
    for j in range(1,arr[0]+1):
        if arr[j] > avg:
            cnt += 1
    print(f'{(cnt / arr[0]) * 100:.3f}%')
    ans = 0
    cnt=0
    total = 0
    avg = 0

