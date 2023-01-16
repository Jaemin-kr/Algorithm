import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split()) #수빈, 동생 위치
max_num = 100000 #이동할 수 있는 최대 위치
visited = [0]*(max_num+1)

def bfs():
    q = deque()
    q.append(n) #수빈의 출발 위치를 규에 삽입
    while q:
        x = q.popleft()
        #수빈의 위치가 동생의 위치와 같으면 종료
        if x == k:
            print(visited[x])
            break
        #수빈이 이동할 수 있는 방향
        #이동할 위치가 범위 내이고 아직 방문하지 않았으면 방문
        for j in (x-1,x+1,x*2):
            if 0 <= j <= max_num and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)

bfs()
