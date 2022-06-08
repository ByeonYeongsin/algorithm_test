# 완전 이진 트리
import sys

def traverse(start, end, level):
    if start == end:
        tree[level].append(tree[start])
        return
    center = (start + end) // 2
    tree[level].append(node[center])
    traverse(start, center-1, level+1)
    traverse(center+1, end, level+1)

K = int(sys.stdin.readline().strip())
node = list(map(int, sys.stdin.readline().strip().split()))
tree = [[] for _ in range(K)]

traverse(0, len(node)-1, 0)

for n in tree:
    print(*n)