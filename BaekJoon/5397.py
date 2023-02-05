import sys

T = int(sys.stdin.readline())
ans = []
cursor = 0
for _ in range(T):
    pwd = list(map(str, sys.stdin.readline()))

print(pwd[0])

for i in range(len(pwd)):
    if pwd[i] == '<':
        if len(ans) != 0:
            cursor -= 1
        else:
            continue
    elif pwd[i] == '-':
        if len(ans) != 0:
            ans.pop()
        else:
            continue
    