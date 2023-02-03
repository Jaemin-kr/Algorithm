N = int(input())
k = 2*(N-1)
for i in range(1,N+1):
    if i == 1:
        print(' '*(N-i)+"*"*1)
    else:
        print(' '*(N-i)+"*"*(2*i-1))

for j in range(N-1,0,-1):
    if i == 1:
        print(' '*(N-j)+"*"*1)
    else:
        print(' '*(N-j)+"*"*(2*j-1))