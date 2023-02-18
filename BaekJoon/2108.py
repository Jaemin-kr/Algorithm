import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

new_arr = sorted(arr)
common = Counter(new_arr).most_common()
print(int(round(sum(arr)/n,0)))
if n == 1:
    print(new_arr[0])
    print(new_arr[0])
    print('0')
else:
    print(new_arr[int((n-1)/2)])
    if common[0][1] == common[1][1]:
        print(common[1][0])
    else:
        #print("최빈값",common)
        print(common[0][0])
    print(new_arr[-1] - new_arr[0])

    #https://codepractice.tistory.com/71