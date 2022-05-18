# 트리와 쿼리

from lib2to3.pytree import Node
import sys

N, R, Q = map(int, sys.stdin.readline().strip().split())
tree = [[] for _ in range(N+1)]
node_count = [0 for _ in range(N+1)]

def dfs(node):
    node_count[node] = 1
    for child_node in tree[node]:
        if not node_count[child_node]:
            dfs(child_node)
            node_count[node] += node_count[child_node]

for i in range(N-1):
    U, V = map(int, sys.stdin.readline().strip().split())
    tree[U].append(V)
    tree[V].append(U)

dfs(R)

for i in range(Q):
    U = int(sys.stdin.readline().strip())
    print(node_count[U])
