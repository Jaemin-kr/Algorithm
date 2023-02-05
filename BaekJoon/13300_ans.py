import sys
input=sys.stdin.readline
M=[0,0,0,0,0,0]
N=[0,0,0,0,0,0]
s=0
a,b=map(int,input().split())
for i in range(a):
    c,d=map(int,input().split())
    if c==1:
        M[d-1]+=1
    if c==0:
        N[d-1]+=1
        
        
for i in range(6):
    if M[i]%b==0:
        s+=M[i]//b
    else:
        s+=M[i]//b+1
    if N[i]%b==0:
        s+=N[i]//b
    else:
        s+=N[i]//b+1
print(s)