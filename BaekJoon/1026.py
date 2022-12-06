t = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


c = sorted(a, reverse=True)
d = sorted(b)

ans = 0
for i in range(t):
    ans += c[i] * d[i]
print(ans)
