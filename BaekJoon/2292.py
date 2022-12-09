#벌집
n = int(input())

bee_home = 1
cnt = 1

while n > bee_home:
    bee_home += 6*cnt
    cnt += 1
print(cnt)