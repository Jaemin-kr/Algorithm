import sys

cctv_map = []
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    cctv_map.append(list(map(int, sys.stdin.readline().split())))

print(cctv_map)

dx = [1,-1,1,-1,1,0]
dy = [0,0,0,0,0,1]