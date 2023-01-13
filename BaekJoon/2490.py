import sys

for i in range(3):
    b = 0
    a = list(map(int, sys.stdin.readline().split()))
    b = a.count(1)
    if b == 1:
        print('C')
    elif b == 2:
        print('B')
    elif b == 3:
        print('A')
    elif b == 4:
        print('E')
    else:
        print('D')
