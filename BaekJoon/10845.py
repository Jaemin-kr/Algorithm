import sys

queue = []
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
    if cmd[0] == "push":
        queue.append(cmd[1])
        tail += 1
    elif cmd[0] == "pop":
        if is_empty(queue) == 1:
            print(-1)
        else:
            #print(queue)
            print(queue.pop(0))
            head += 1
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] =="empty":
        print(is_empty(queue))
    elif cmd[0] == "front":
        if is_empty(queue) == 1:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0] == "back":
        if is_empty(queue) == 1:
            print(-1)
        else:
            print(queue[-1])

# tail, head index error
