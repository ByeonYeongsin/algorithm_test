# 행성 연결
import sys

def find_parent(parent, x):  # 부모 노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):  # 집합 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline().strip().split())  # 행성의 수
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]  # 각 행성간의 플로우 관리 비용
parent = [i for i in range(n)]  # 부모 노드 정보
edges = []  # 행성 간선 정보 # 삼각형 대칭

for i in range(1, n):
    for j in range(i):
        edges.append((arr[i][j], i, j))
edges.sort()

answer = 0
for cost, a, b in edges:  # 크루스칼 알고리즘 수행
    if find_parent(parent, a) != find_parent(parent, b):  # 서로 같은 집합이 아닌 경우
        union(parent, a, b)  # 연결
        answer += cost

print(answer)  # 최소 플로우의 관리 비용