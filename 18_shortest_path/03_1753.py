# 최단경로
import sys
import heapq

V, E = sys.stdin.readline().strip().split()
K = sys.stdin.readline().strip().split()
dist = [float('inf')] * (V)
linked = [[] for i in range(V)]
for _ in range(E):
    u, v, w = sys.stdin.readline().strip().split()
    linked[u-1].append((v-1, w))

heap = []
heapq.heappush(heap, (0, K-1))

while(heap):
    now_dist, now_node = heapq.heappop(heap)
    if dist[now_node] > now_dist:
        for next_node, next_dist in linked[now_node]:
            d = now_dist + next_dist
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(heap, (d, next_node))
            
for i in dist:
    print(i if i != float('inf') else "INF")

