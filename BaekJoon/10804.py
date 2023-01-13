arr = [i for i in range(21)]
for _ in range(10):
    str, end = map(int,input().split())
    arr[str:end+1] = arr[end:str-1:-1]

print(arr)