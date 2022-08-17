# 도시 분할 계획
import sys

def find_parents(parents, x): # 특정 노드가 속한 집합 찾기
    if parents[x] != x:
        return find_parents(parents, parents[x])
    return parents[x]

def union_parent(parents, A, B): # 두 노드가 속한 집합 합치기
    a = find_parents(parents, A)
    b = find_parents(parents, B)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N, M = map(int, sys.stdin.readline().strip().split())
roads = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    roads.append((C, A, B))

roads = sorted(roads) # C로 정렬될 수 있도록
cost = 0
parents = [i for i in range(N+1)]
for c, a, b in roads:
    if find_parents(parents, a) != find_parents(parents, b): # 두 노드가 같은 집합이 아닌 경우에 연결한다.
        union_parent(parents, a, b)
        cost += c # 연결한 도로의 비용을 누적
        last = c # 마지막에 연결한 도로의 비용을 저장
print(cost - last)