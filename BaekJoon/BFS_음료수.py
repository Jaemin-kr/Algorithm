import sys
from collections import deque

#input = sys.stdin.readline

n,m = map(int, input().split())
board = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    board.append(list(map(int,input())))


def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    if board[x][y] == 1:
        return False

    while queue:
        x, y = queue.popleft()
        board[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                queue.append((nx,ny))

    return True

cnt = 0

for i in range(n):
    for j in range(m):
        if bfs(i,j) == True:
            cnt += 1

print(cnt)



