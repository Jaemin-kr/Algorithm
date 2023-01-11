
a = list(map(int,input().split()))
for i in range(len(a)):
    if a[i] < 0:
        if a[i]%2 == 0:
            print("A")
        else:
            print('B')
    else:
        if a[i]%2 == 0:
            print('C')
        else:
            print("D")