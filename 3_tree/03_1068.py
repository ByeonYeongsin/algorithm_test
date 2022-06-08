# 트리
import sys

def dfs(removed_node):
    global arr
    arr[removed_node] = -2
    for i in range(len(arr)):
        if arr[i] == removed_node:
            dfs(i)

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
removed_node = int(sys.stdin.readline().strip())
leaf_node_num = 0

dfs(removed_node)

for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        leaf_node_num += 1
print(leaf_node_num)