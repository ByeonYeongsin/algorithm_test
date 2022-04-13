# dfs와 bfs
import sys

n, m, v = map(int, sys.stdin.readline().split())
matrix = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(n):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if (visited[i] == 0 and matrix[v][i] == 1):
            dfs(i)

def bfs(n):
    queue = [n]
    visited[n] = 0
    while queue:
        v = queue.pop(0)
        print(v, end = ' ')
        for i in range(1, n+1):
            if(visited[i] == 1 and matrix[v][i] == 1):
                queue.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)