T = int(input())

for _ in range(T):
    arr = list(input())
    cnt = 0
    sum_cnt = 0
    for i in arr:
        if i == 'O':
            cnt += 1
            sum_cnt += cnt
        else:
            cnt = 0
    print(sum_cnt)