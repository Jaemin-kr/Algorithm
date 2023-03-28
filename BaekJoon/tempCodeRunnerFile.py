import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
ans = []
stack = []


for i in range(n):
    while stack:
        if stack[-1][1] > tower[i]:
            ans.append(stack[-1][0]+1)
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, tower[i]])

print("".join(map(str, ans)))
    