# 여행 가자
from pickle import FALSE, TRUE
import sys
sys.setrecursionlimit(1000000)

from torch import true_divide

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
cities = []
for _ in range(n):
    cities.append(list(map(int, sys.stdin.readline().strip().split())))
city_parent = [i for i in range(n+1)]

def get_parent(n):
    if city_parent[n] != n:
        city_parent[n] = get_parent(city_parent[n])
    return city_parent[n]

for i in range(n):
    for j in range(i+1, n):
        if int(cities[i][j]) == 1:
            city_parent[get_parent(j)] = get_parent(i)

plan = set(get_parent(map(int, sys.stdin.readline().strip().split())))
flag = 1
# for i in range(m-1):
#     if city_parent[get_parent(plan[i]-1)] != city_parent[get_parent(plan[i+1]-1)]:
#         flag = 0
#         print('NO')
#         break
# if flag == 1:
#     print('YES')
if len(plan) == 1:
    print('YES')
else:
    print('NO')
