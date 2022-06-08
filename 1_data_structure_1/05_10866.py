# 덱
import sys
from collections import deque

dq = deque()
N = int(sys.stdin.readline().strip())

for _ in range(N):
    comm = sys.stdin.readline().strip().split()

    if comm[0] == 'push_front':
        dq.appendleft(comm[1])
    elif comm[0] == 'push_back':
        dq.append(comm[1])
    elif comm[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif comm[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif comm[0] == 'size':
        print(len(dq))
    elif comm[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif comm[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
    elif comm[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)