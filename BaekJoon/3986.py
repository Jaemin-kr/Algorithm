T = int(input())
cnt = 0

for _ in range(T):
    stack = []
    word = input().rstrip()

    for i in range(len(word)):
        if stack and word[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(word[i])
    if not stack:
        cnt += 1

print(cnt)
