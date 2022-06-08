# 덱
import sys
from collections import deque

q = deque()
N = int(sys.stdin.readline().strip())

for _ in range(N):
    comm = list(sys.stdin.readline().strip().split())
    if comm[1] :
        comm[1] = int(comm[1])
    if comm[0] == 'push_front':
        deque.appendleft(comm[1])
    elif comm[0] == 'push_back':
        deque.append(comm[1])
    elif comm[0] == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif comm[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif comm[0] == 'size':
        print(len(deque))
    elif comm[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif comm[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)