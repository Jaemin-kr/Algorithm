from itertools import permutations
import sys

n, m = map(int,sys.stdin.readline().split())
arr = []
for i in range(1,n+1,):
    arr.append(i)
permu = list(permutations(arr,m))

for i in range(len(permu)):
    print(permu[i])