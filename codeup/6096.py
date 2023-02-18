
# board = []
# for i in range(20):
#     board.append([])
#     for j in range(20):
#         board[i].append(0)

d=[]
for i in range(20) :
    d.append([])
    for j in range(20) :
        d[i].append(0)

for i in range(19) :
    a = input().split()
    for j in range(19) :
        d[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
    x,y=input().split()
    x=int(x)
    y=int(y)
    for j in range(1, 20) :
        if d[j][y]==0 :
            d[j][y]=1
        else :
            d[j][y]=0

        if d[x][j]==0 :
            d[x][j]=1
        else : d[x][j]=0

for i in range(1, 20) :
    for j in range(1, 20) :
        print(d[i][j], end=' ')
    print()
# n = int(input())
# for i in range(n):
#    x, y = input().split()
        # if board[j][int(x0
        # 0)]==0:
        #   board[j][int(x)] = 1
        # else:
        #    board[j][int(x)] = 0
        # if board[int(x)][j] == 0:
        #    board[int(x)][j] = 1
        # else:
        #    board[int(x)][j] = 0

# for i in range(1, 20) :
#   for j in range(1, 20) : 
#     print(board[i][j], end=' ')    #공백을 두고 한 줄로 출력
#   print()                          #줄 바꿈