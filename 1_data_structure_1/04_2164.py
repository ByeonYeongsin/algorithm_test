# 카드2

from collections import deque

queue = deque()
N = int(input())
for i in range(1,N+1):
    queue.append(i)

while True:
    a = queue.popleft()
    if not queue: # 여기서 확인
        print(a)
        break
    b = queue.popleft()
    queue.append(b)