a, b, c = list(map(int,input().split()))
d = ((a if a<b else b) if ((a if a>b else b)<c) else (b if b<c else c))
print(int(d))
