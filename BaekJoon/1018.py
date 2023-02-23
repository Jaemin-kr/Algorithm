n, m =map(int,input().split())

board = []
ans = []
for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        black = 0
        white = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] != 'B':
                        black += 1
                    if board[x][y] != 'W':
                        white += 1
                else:
                    if board[x][y] != 'W':
                        black += 1
                    if board[x][y] != 'B':
                        white += 1

        ans.append(black)
        ans.append(white)

print(min(ans))