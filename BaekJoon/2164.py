import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
card = deque(range(1,N+1))

#print(card)
while True:
    if len(card) == 1:
        break
    card.popleft()
    card.rotate(-1)


print(card[0])