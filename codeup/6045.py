import sys

a, b, c = map(int, sys.stdin.readline().split())
sum = a+b+c
print(sum, format(float(sum/3), '.2f'))