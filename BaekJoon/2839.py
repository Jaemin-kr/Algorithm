N = int(input())
cnt = 0
while N >= 0:
    if N % 5 == 0:
        cnt += N//5
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)
#
# if N%5 != 0 and N%3 != 0:
#     print(-1)
# else:
#     cnt = N//5
#     if N%5 == 0:
#         print(cnt)
#     else:
#         new_N = N - 5*(N//5)
#         cnt1 = new_N//3
#         print(cnt+cnt1)