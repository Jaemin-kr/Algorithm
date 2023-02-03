N = int(input())
k = 2*(N-1)
for i in range(N,0,-1):
    if i == 1:
        print(' '*(N-i)+"*"*1)
    else:
        print(' '*(N-i)+"*"*(2*i-1))

for i in range(1,N+1):
    if i==1:
        continue
    print(' '*(N-i)+"*"*(2*i-1))