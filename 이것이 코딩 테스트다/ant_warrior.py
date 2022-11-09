#개미전사

n = int(input())
store_house = list(map(int, input().split()))

d = [0] * 100

d[0] = store_house[0]
d[1] = max(d[0], store_house[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + store_house[i])

print(d[n-1])
