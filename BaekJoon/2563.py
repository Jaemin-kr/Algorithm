import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
board = [[0] * 100 for _ in range(100)]
#가로, 세로 각각 100

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            #print("x, y",x, y)
            board[j][k] = 1

for i in range(100):
    for j in range(100):
        print(board[i][j], end=' ')
        if board[i][j] == 1:
            cnt += 1
    print()

print(cnt)
#색종이 영역 넓이
