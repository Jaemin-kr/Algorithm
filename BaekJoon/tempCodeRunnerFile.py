
xy = []
n = int(input())

for i in range(n):
    cord = list(map(int,input().split()))
    xy.append(cord)

xy = sorted(xy)
#print(xy)
for i in range(n):
    xy_str = str(xy[i])[1:-1]
    print(xy_str.replace(",",""))