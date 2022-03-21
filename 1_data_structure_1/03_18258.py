# 큐2

from collections import deque

queue = deque() # deque
N = int(input())
for i in range(N):
    com = input().split() # 배열로
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif com[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)