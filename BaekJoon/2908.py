import sys

input = sys.stdin.readline
new_a = []
new_b = []
a, b = map(int,input().split())
for i in range(3):
    new_a.append(a%10)
    a = a//10
    new_b.append(b%10)
    b = b//10


if new_a[0] > new_b[0]:
    print("".join(map(str,new_a)))
elif new_a[0] < new_b[0]:
    print("".join(map(str,new_b)))
else:
    if new_a[1] > new_b[1]:
        print("".join(map(str,new_a)))
    elif new_a[1] < new_b[1]:
        print("".join(map(str,new_b)))
    else:
        if new_a[2] > new_b[2]:
            print("".join(map(str,new_a)))
        elif new_a[2] < new_b[2]:
            print("".join(map(str,new_b)))