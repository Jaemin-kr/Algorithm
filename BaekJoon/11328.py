T = int(input())
for _ in range(T):
    a, b = input().split()
    cnt = [0]*26
    cnt1 = [0]*26
    ans = 0
    for i in a:
        cnt[ord(i) - 97] += 1
    for i in b:
        cnt1[ord(i) - 97] += 1

    for i in range(26):
        ans += abs(cnt[i] - cnt1[i])
    if ans == 0:
        print("Possible")
    else:
        print("Impossible")
