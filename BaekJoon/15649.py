import sys

n, m = map(int,sys.stdin.readline().split())
arr = []
isused = [False] * 10

#permu = list(permutations(arr,m))

def func():
    if len(arr)==m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1,n+1):
        if isused[i]:
            continue
        isused[i] = True
        arr.append(i)
        func()
        arr.pop()
        #print(arr)
        #print(isused)
        isused[i] = False

func()

'''
import itertools

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

array = itertools.permutations(nums, m)

for i in array:
    for j in i:
        print(j, end = ' ')
    print()
'''
        
