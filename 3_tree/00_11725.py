# 트리의 부모 찾기

import sys

N = int(sys.stdin.readline().strip())
parent_node = [1]
nodes = []

for _ in range(N-1):
    t1, t2 = map(int, sys.stdin.readline().strip().split())
    if t1 in parent_node:
        nodes.append([t1, t2])
        parent_node.append(t2)
    elif t2 in parent_node:
        nodes.append([t2, t1])
        parent_node(t1)

nodes.sort(key=lambda x:x[1])
for node in nodes:
    print(node[0])
