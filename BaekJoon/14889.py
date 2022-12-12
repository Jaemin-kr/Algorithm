def cal_diff(team1, team2):
    sum1 = 0
    sum2 = 0

    for i in range(len(team1)):
        for j in range(len(team2)):
            sum1 += arr[team1[i]][team1[j]]
            sum2 += arr[team2[i]][team2[j]]
    return abs(sum1 - sum2)

def make_team(team1, cnt, N, start):
    global ans

    if cnt == N//2:
        team2 =[]
        for i in range(N):
            if i not in team1:
                team2.append(i)

        local_diff = cal_diff(team1, team2)
        ans = min(ans, local_diff)
        return

    for i in range(start, N):
        if i not in team1:
            team1.append(i)
            make_team(team1, cnt+1, N, i+1)
            team1.remove(i)

if __name__=="__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = int(1e9)
    make_team([], 0, N, 0)

    print(ans)

