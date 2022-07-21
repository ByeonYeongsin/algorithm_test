# 끝나지 않는 파티
import sys

N, M = map(int, sys.stdin.readline().strip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][i] + graph[i][k] < graph[j][k]:
                graph[j][k] = graph[j][i] + graph[i][k]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    if graph[A-1][B-1] <= C:
        print('Enjoy other party')
    else:
        print('Stay here')