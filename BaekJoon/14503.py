
N, M = map(int, input().split())


visited = [[0] * M  for _ in range(N)]
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
#d의 방향은 N, W, S, E  0->3->2->1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


visited[r][c] = 1
cnt = 1

while 1:
    flag = 0

    for _ in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]

        d = (d+3)%4

        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny

                flag = 1
                break
    if flag == 0:
        if room[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r,c = r-dx[d], c-dy[d]

