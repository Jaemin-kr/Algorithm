import sys
from collections import deque

T = int(sys.stdin.readline())


for _ in range(T):
    front = deque()
    back = deque()

    for item in input():
        if item == '<':
            if front:
                back.appendleft(front.pop())
        elif item == '>':
            if back:
                front.append(back.popleft())
        elif item == '-':
            if front:
                front.pop()
        else:
            front.append(item)
    front.extend(back)
    print(''.join(front))
