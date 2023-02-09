n = int(input())
item = []

for _ in range(n):
    item.append(list(input().split()))

item.sort(key=lambda a:int(a[0]))

for i in range(n):
    print(item[i][0], item[i][1])