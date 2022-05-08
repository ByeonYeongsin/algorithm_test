# 최소 스패닝 트리
import sys

v, e = map(int, sys.stdin.readline().strip().split())

vertex = [[-1] * (v+1) for _ in range(v+1)]
visited = [0] * (v+1)
mst_sum = 0

for _ in range(v):
    frm, to, edge = map(int, sys.stdin.readline().strip().split())
    vertex[frm][to] = edge

def mst(node):
    global mst_sum
    visited[node] = 1
    new_node = -1
    now_cost = -1
    for i in range(1, v+1):
        if vertex[node][i] != -1 and visited[i] != 1:
            now_cost = vertex[node][i]
            new_node = i
    for i in range(new_node, v+1):
        if vertex[node][i] != -1 and visited[i] != 1 and vertex[node][i] < now_cost:
            now_cost = vertex[node][i]
            new_node = i
    
    if new_node == -1:
        print(mst_sum)
    else:
        mst_sum += vertex[node][new_node]
        mst(new_node)

mst(1)