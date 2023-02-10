import sys

num = list(map(int,sys.stdin.readline().split()))
list_sum = 0
for i in range(5):
    list_sum += num[i]**2

print(list_sum%10)