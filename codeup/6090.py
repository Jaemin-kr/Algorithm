a, m, d, n = map(int, input().split())
ans = 0
for i in range(1, n+1):
    print("before ans", ans)
    if n == 1:
        print(a)
    elif i == n:
        print(ans)
    ans = a*(m)+d
    a = ans


#print(ans)