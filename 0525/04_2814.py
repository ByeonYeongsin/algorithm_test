# 최장 경로

import sys

def dfs(node, path_len):
    global max_len
    visited[node] = 0
    path_len += 1
    if max_len < path_len:
        max_len = path_len
    for i in graph[node]:
        if visited[i]:
            dfs(i, path_len)
    visited[node] = 1

f = open("C:/algorithm_test/0525/input/04_input.txt", 'r')
T= int(f.readline().strip())
for t in range(T):
    N, M = map(int, f.readline().strip().split())
    graph = [[] for _ in range(N+1)]
    visited=[1 for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, f.readline().strip().split())
        graph[x].append(y)
        graph[y].append(x)
    
    max_len = 0
    for node in range(N):
        dfs(node, 0)

    print('#', t+1, ' ', max_len, sep='')