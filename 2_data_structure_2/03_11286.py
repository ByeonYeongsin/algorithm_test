# 절대값 힙

import sys
import heapq

N = int(sys.stdin.readline().strip())
h = []

for i in range(N):
    now_num = int(sys.stdin.readline().strip())
    if now_num == 0:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
    else:
        heapq.heappush(h, [abs(now_num), now_num]) 

# [] 배열로 heap정렬하면 0, 1, 2 ... 순으로 정렬되는 것인가?  
