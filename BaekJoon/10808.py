arr = input()
cnt = [0]*26
#i=0 ~ arr까지,  
for i in arr:
    print(ord(i))
    cnt[ord(i) - 97] += 1
    #a의 아스키  코드는 97이므로 cnt의 인덱스 0을 a, 1을 b ... z를 25로 처리

print(*cnt)
print(cnt)