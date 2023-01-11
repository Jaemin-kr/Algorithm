import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
#que size, pop number

idx = list(map(int, sys.stdin.readline().split()))
deq = deque([i for i in range(1, N+1)])
# 연산 1: popleft
# 연산 2: rotate(1)
# 연산 3: rotate(-1)

cnt = 0

def operand1(Q):
    Q.popleft()

def operand2(Q):
    global cnt
    Q.rotate(1)
    cnt += 1

def operand3(Q):
    global cnt
    Q.rotate(-1)
    cnt += 1

# for i in range(N):
#     deq.append(i)

for i in idx:
    while True:
        if deq[0] == i:
            operand1(deq)
            break
        else:
            if deq.index(i) < len(deq)/2:
                while deq[0] != i:
                    operand3(deq)
            else:
                while deq[0] != i:
                    operand2(deq)

print(cnt)

#https://velog.io/@goplanit/Algorithm-%EB%B0%B1%EC%A4%80-1021%EB%B2%88-%ED%9A%8C%EC%A0%84%ED%95%98%EB%8A%94-%ED%81%90%ED%8C%8C%EC%9D%B4%EC%8D%AC