# 최대 힙

import sys
import heapq # 힙

N = int(sys.stdin.readline().strip())
h = []

for i in range(N):
    now_num = int(sys.stdin.readline().strip())
    if now_num != 0:
        heapq.heappush(h, -now_num)
    else:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)

# heapq.heappush(heap, -num), -heapq.heappop(h) => 최대힙 513000 # 5 3 1
# heapq.heappush(heap, num), heapq.heappop(h) => 최소힙 513000 # 1 3 5