N = int(input())
k = 2*(N-1)
for i in range(1,N+1):
    print('*'*(i)+" "*(2*N-2*i)+'*'*(i))

for j in range(N-1,0,-1):
        print('*'*j+" "*(2*(N-j))+'*'*j)