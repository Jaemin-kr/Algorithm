# arr1, arr2 = [], []
# m, n = list(map(int,input().split()))
# arr1 = [list(map(int, input().split())) for _ in range(n)]
# arr2 = [list(map(int, input().split())) for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         print(arr1[i][j] + arr2[i][j], end=' ')
#     print()
#
A, B = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)

for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()