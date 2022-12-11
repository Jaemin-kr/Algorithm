H, M = map(int, input().split())
time = int(input())

hour = (M+time)//60
min = (M+time)%60

if(M + time >= 60):
    if(H+hour >= 24):
        H = H - 24
    H = H + hour
    print(H, min)
else:
    if(H >= 24):
        H = H - 24
    print(H, M+time)