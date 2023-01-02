# from itertools import combinations

# N = int(input())
# arr = list(map(int, input().split()))
# X = int(input())
# cnt = 0
# combi = list(combinations(arr, 2))

# for i in range(len(combi)):
#     #print(combi[i])
#     if X == sum(combi[i]):
#         cnt += 1
# print(cnt)


#투 포인터
N = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr.sort()
left, right = 0, N-1
cnt = 0

while left < right:
    if (arr[left] + arr[right]) == X:
        cnt += 1
    elif(arr[left] + arr[right]) < X:
        left += 1
        continue #없으면 한번만 하고 멈춤
    right -= 1

print(cnt)

