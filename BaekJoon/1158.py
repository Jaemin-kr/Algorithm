N, K = map(int,input().split())

arr = list(range(1, N+1))
idx = K-1
arr1 = []

# for i in range(int(N)):
#     arr.append(1)
# -> list(range(1, N+1)) 로 구현가능
while True:
    arr1.append(arr[idx])
    arr = arr[:idx] + arr[idx+1:]
    if not arr:
        break
    idx = (idx + K-1) % len(arr)

print('<'+', '.join(list(map(str, arr1))) + '>')