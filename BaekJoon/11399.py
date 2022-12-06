T = int(input())
Time = list(map(int, input().split()))
arr = sorted(Time)
ans = 0

for i in range(T):
    for j in range(i+1):
        ans += arr[j]

print(ans)
