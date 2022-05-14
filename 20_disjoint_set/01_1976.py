# 여행 가자
import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
city_parent = [i for i in range(n)]

def union(x, y):
    x = get_parent(x)
    y = get_parent(y)
    if x < y :
        city_parent[y] = x
    else:
        city_parent[x] = y

def get_parent(n):
    if city_parent[n] != n:
        city_parent[n] = get_parent(city_parent[n])
    return city_parent[n]

for i in range(n):
    link = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(n): # 왜 (i+1, n)은 안되는지
        if link[j] == 1:
            union(i, j)

plan = map(int, sys.stdin.readline().strip().split())
plan_set = []
for now_plan in plan:
    plan_set.append(city_parent[now_plan-1])
plan_set = set(plan_set)

if len(plan_set) == 1:
    print('YES')
else:
    print('NO')
