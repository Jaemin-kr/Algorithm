import sys
man_1, woman_1 = 0, 0
man_2, woman_2 = 0, 0
man_3, woman_3 = 0, 0
man_4, woman_4 = 0, 0
man_5, woman_5 = 0, 0
man_6, woman_6 = 0, 0
cnt = 0
N, K = map(int, sys.stdin.readline().split())

for i in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    
    if S == 1:
        #print(S)
        if Y == 1:
            man_1 += 1
        elif Y == 2:
            man_2 += 1
        elif Y == 3:
            man_3 += 1
        elif Y == 4:
            man_4 += 1
        elif Y == 5:
            man_5 += 1
        elif Y == 6:
            man_6 += 1
    elif S == 0:
        if Y == 1:
            woman_1 += 1
        elif Y == 2:
            woman_2 += 1
        elif Y == 3:
            woman_3 += 1
        elif Y == 4:
            woman_4 +=1
        elif Y == 5:
            woman_5 += 1
        elif Y == 6:
            woman_6 += 1
# print("Man: ",man_1,man_2,man_3,man_4,man_5,man_6)
# print("Woan: ",woman_1,woman_2,woman_3,woman_4,woman_5,woman_6)
Man = [man_1,man_2,man_3,man_4,man_5,man_6]
Woman = [woman_1,woman_2,woman_3,woman_4,woman_5,woman_6]
for i in range(6):
    if Man[i]%K == 0:
        cnt += Man[i]//K
        #print(cnt, "case1 man_",i)
    elif Man[i]%K != 0:
        cnt += (Man[i]//K)+1
        #print(cnt, "case2 man_",i)

for j in range(6):
    if Woman[j]%K == 0:
        cnt += Woman[j]//K
        #print(cnt,"case3 woman_",j)
    elif Woman[j]%K != 0:
        cnt += (Woman[j]//K)+1
        #print(cnt,"case4 woman_",j)

print(cnt)


