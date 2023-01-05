import sys
from collections import deque


deq = deque()
N = int(input())
head, tail = 0, 0

def is_empty(Q):
    if len(Q) != 0:
        #not empty
        return 0
    else:
        # empty
        return 1

for _ in range(N):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "push_front":
        deq.appendleft(cmd[1])
        tail += 1
    elif cmd[0] == "push_back":
        deq.append(cmd[1])
    elif cmd[0] == "pop_front":
        if is_empty(deq) == 1:
            print(-1)
        else:
            print(deq.popleft())        
    elif cmd[0] == "pop_back":
        if is_empty(deq) == 1:
            print(-1)
        else:
            print(deq.pop())
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] =="empty":
        print(is_empty(deq))
    elif cmd[0] == "front":
        if is_empty(deq) == 1:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0] == "back":
        if is_empty(deq) == 1:
            print(-1)
        else:
            print(deq[-1])

