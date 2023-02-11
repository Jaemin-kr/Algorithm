import sys

input = sys.stdin.readline
xy = []
n = int(input())
for i in range(n):
    cord = list(map(int, input().split))
    xy.append(cord)

print(xy.sort())