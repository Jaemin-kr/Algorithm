import sys

a, b = map(int, sys.stdin.readline().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(float(a/b), '.2f'))