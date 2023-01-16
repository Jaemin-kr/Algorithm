import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())

graph = []

que = deque()
que1 = deque()

visited = [[0]*c for _ in range(r)]
visited1 = [[0]*c for _ in range(r)]


for i in range(r):
    temp = list(input())

    for j in range(len(temp)):
        if temp[j] == "J":
            que.append((i,j))
            visited[i][j] = 1
        
        elif temp[j] == "F":
            que1.append((i,j))
            visited1[i][j] = 1
    graph.append(temp)
#graph = [list(map(int, input())) for _ in range(N)]

#print(graph)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while que1:
        x, y = que1.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if not visited1[nx][ny] and graph[nx][ny] != "#":
                    visited1[nx][ny] = visited1[x][y]+1
                    que1.append((nx,ny))
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != "#" and not visited[nx][ny]:
                    if not visited1[nx][ny] or visited1[nx][ny] > visited[x][y] + 1:
                        visited[nx][ny] = visited[x][y] + 1
                        que.append((nx,ny))
            else:
                return visited[x][y]
    return "IMPOSSIBLE"

print(bfs())
