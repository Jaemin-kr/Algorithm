N = int(input()) #N입력

T = [] #T 저장할 배열
P = [] #P 저장할 배열
dp = [] #dp 저장할 배열

for i in range(N):
    a, b = map(int, input().split()) #Ti, Pi의 값을 입력
    #T, P의 값을 배열에 저장
    T.append(a)
    P.append(b)
    dp.append(b)
dp.append(0) #N+1일

print(dp)
#range(start, stop, step)
for i in range(N-1, -1, -1): #N-1 ~ -1까지 -1씩 감소
    #print("i의 값 변화"+str(i))
    if T[i] + i > N: #T[N-1] + N-1의 값이 N보다 크면
        dp[i] = dp[i+1] #결과를 그대로 이동
    else: #이외의 경우
        print('else i value: '+str(i))
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]]) #dp값은 이전 dp값과 비교
print(dp[0])