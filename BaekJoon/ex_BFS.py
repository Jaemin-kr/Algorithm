from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True #현재노드를 방문처리
    
    while queue: #queue가 빌때까지 반복
        v = queue.popleft() #큐에서 pop - FIFO
        print(v, end=' ')

        for i in graph[v]: #그래프 탐색
            if not visited[i]: #만약 방문하지 않았으면
                queue.append(i) #큐에 삽입
                visited[i] = True

graph = [[], 
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]
#방문정보
visited = [False]*9

bfs(graph,1,visited)

