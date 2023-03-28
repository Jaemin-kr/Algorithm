from collections import deque
import sys

input = sys.stdin.readline

dx = [2,1,-1,-2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]



def bfs(x1, y1, x2, y2):
    queue = deque()
    queue.append([x1,y1])
    visited[x1][y1] = 1

    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            print(visited[x2][y2] - 1)
            return
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < length and 0 <= ny < length and visited[nx][ny] == 0:
                queue.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1

T = int(input())
for i in range(T):
    length = int(input())
    x1, y1 = map(int,input().split())
    x2, y2 = map(int,input().split())
    visited = [[0] * length for i in range(length)]
    bfs(x1,y1,x2,y2)