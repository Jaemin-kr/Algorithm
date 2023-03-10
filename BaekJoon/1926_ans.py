import sys
from collections import deque

input = sys.stdin.readline

board = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n, m = map(int,input().split())
num = 0
max_area = 0
for i in range(n):
    board.append(list(map(int,input().split())))

print(board)

def bfs():
#board = [[0] * 10 for _ in range(10)]

# board = []
# for i in range(10):
#     board.append(list(map(int, input().split())))
