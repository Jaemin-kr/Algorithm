w, h, b = map(int,input().split())
ans = w*h*b/8/1024/1024
print(f'{ans:.2f} MB')