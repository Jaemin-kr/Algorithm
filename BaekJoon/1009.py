'''
1,1,1,1
2,4,8,6 2,4,8,6,
3,9,7,1 3
4,
'''

t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    a = a%10

    if a == 0:
        print(0)
    elif a in [1,5,6]:
        print(a)
    elif a in [4,9]:
        b = b%2
        if b == 0:
            print(a*a%10)
        else:
            print(a)
    else:
        b = b%4
        if b == 0:
            print(a**4%10)
        else:
            print(a**b%10)