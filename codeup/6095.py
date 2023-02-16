

board = []
for i in range(20):
    board.append([])
    for j in range(20):
        board[i].append(0)

n = int(input())
for i in range(n):
    x, y = input().split()
    board[int(x)][int(y)] = 1

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(board[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()                          #줄 바꿈