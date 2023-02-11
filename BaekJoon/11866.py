n, k = map(int,input().split())
arr = list(range(1,n+1))
idx = k-1
ans = []
print(arr[:idx], arr[idx+1:])
while True:
    ans.append(arr[idx])
    arr = arr[:idx] + arr[idx+1:] #arr[idx]제외하고 새로 만듦
    if not arr:
        break
    idx = (idx+k-1) % len(arr)


print('<'+','.join(list(map(str,ans)))+'>')

