#list queue
queue = [1,2,3,4,5]
print(queue)
queue.append(7)
queue.pop(0)
#pop(1)
print(queue)
#deque(double-ended queue)
#O(N) using linked list
from collections import deque

que = deque([4,5,6])
print(que)
que.append(6)
que.append(3)
print(que)

que.popleft()
que.popleft()

que.appendleft(8)
que.appendleft(10)
print(que)

