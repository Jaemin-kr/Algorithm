h, w = map(int,input().split())
n = int(input())


board = []
for i in range(h):
    board.append([])
    for j in range(w):
        board[i].append(0)

for i in range(n):
    cnt = 0
    length, direction, x, y = map(int,input().split())
    x, y = x-1, y-1
    nx, ny = x, y
    board[x][y] = 1
    for j in range(length):
        print("j and dir",j,direction)
        if direction == 0:
            ny += 1
            if ny >= 0 and ny < h:
                board[x][ny] = 1
                #print("x and ny",x, ny)

        elif direction == 1:
            nx += 1
            if nx >= 0 and nx < w:
                board[nx][y] = 1
                #print("nx and y", nx, y)


for i in range(h) :
    for j in range(w) :
        print(board[i][j], end=' ')
    print()