arr = input()
arr1 = input()
cnt = [0]*26
cnt1 = [0]*26
ans = 0
#i=0 ~ arr까지,  
for i in arr:
    cnt[ord(i) - 97] += 1

for i in arr1:
    cnt1[ord(i) - 97] += 1
    #a의 아스키  코드는 97이므로 cnt의 인덱스 0을 a, 1을 b ... z를 25로 처리

for i in range(26):
    ans += abs(cnt[i] - cnt1[i])

print(ans)