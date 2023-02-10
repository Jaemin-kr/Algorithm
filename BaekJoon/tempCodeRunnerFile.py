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

for i in range(3):
    if new_a[i] > new_b[i]:
        print("".join(map(str,new_a)))
    else:
        print("".join(map(str,new_b)))
