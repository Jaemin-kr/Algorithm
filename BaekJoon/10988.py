import sys

input = sys.stdin.readline
word = list(input().rstrip())
#print(word)
new_word = list(reversed(word))
#print("new",new_word)
cnt = 0
ans = 0
for i in range(len(word)):
    if word[i] == new_word[i]:
        cnt += 1
    else:
        ans = 0

if cnt == len(word):
    print(1)
else: print(ans)
        

