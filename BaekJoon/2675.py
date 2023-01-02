T = int(input())
arr = []
for _ in range(T):
    r, s = input().split()
    r = int(r)
    for i in s:
        print(i*r, end='')
    print()

