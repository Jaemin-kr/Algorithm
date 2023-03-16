import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split()) #n, m 입력
board = [] #2차원 배열 입력 받을 곳

for i in range(n):
    board.append(list(map(int,input().split()))) #도화지 입력

#탐색 순서 (1,0), (0,1) (-1,0) (0,-1)
#          (x, y+1)
#  (x-1,y) (x,y) (x+1,y)
#          (x, y-1)
dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[False] * m for _ in range(n)] # m * n 배열 False로 초기화

def bfs(x,y): #bfs구현
    paint_cnt = 1 #그림 넓이
    queue = deque() 
    queue.append((x,y)) #방문하지 않은 x,y큐에 삽입
    visited[x][y] = 1 #방문한 x,y값을 1로 변경

    while queue: #queue가 차있을 때
        x, y = queue.popleft() #x,y는 큐에서 꺼냄(방문하지 않은 좌표)
        for i in range(4): #x,y 4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            #nx, ny좌표가 n, m의 범위에 들어온다면
            if 0 <= nx < n and 0 <= ny < m:
                # 범위에 들어오고 그림(1)이고 아직 방문하지 않은좌표일 때
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1 #해당좌표를 방문했다교 표시
                    queue.append((nx,ny)) #해당 좌표를 큐에서 꺼냄
                    paint_cnt += 1 #그림의 넓이 +1

    return paint_cnt #그림의 넓이 return

cnt, max_area = 0, 0 #그림 갯수와 가장 큰 넓이를 표시할 변수

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]: #board가 1이고 아직 방문하지 않았을 때
            cnt += 1 #그림 갯수 +1
            max_area = max(max_area, bfs(i,j)) #새로운 그림의 넓이와 기존 그림의 넓이 중 최댓값

#출력
print(cnt)
print(max_area)