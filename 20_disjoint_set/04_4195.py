# 친구 네트워크
import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        number[a] += number[b]
    print(number[a])


for _ in range(int(sys.stdin.readline().strip())):
    num = int(sys.stdin.readline().strip())
    parent, number = {}, {}
    for i in range(num):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] =b
            number[b] = 1
        union(a, b)