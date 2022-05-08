# 집합의 표현
# import sys

# n, m = map(int, sys.stdin.readline().strip().split())
# n_list = [0] * (n+1)
# now_index = 1

# for _ in range(m):
#     ch, a, b = map(int, sys.stdin.readline().strip().split())
#     if ch == 0:
#         if a == b:
#             continue
#         if n_list[a] != 0:
#             now_a = n_list[a]
#             if n_list[b] == 0:
#                 n_list[b] = now_a
#             else:
#                 now_b = n_list[b]
#                 for i in range(n+1):
#                     if n_list[i] == now_b:
#                         n_list[i] = now_a
#                 n_list[b] = now_a
#         elif n_list[b] != 0: # n_list[a]는 0
#             n_list[a] = n_list[b]
#         else:
#             n_list[a] = n_list[b] = now_index
#             now_index += 1
#     else:
#         if n_list[a] != 0 and n_list[b] != 0 and n_list[a] == n_list[b]:
#             print('YES')
#         else:
#             print('NO')

import sys 
sys.setrecursionlimit(1000000)

n, m = map(int, sys.stdin.readline().strip().split())
parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x]) # 이해, 중요
    return parent[x]

for _ in range(m):
    ch, a, b = map(int, sys.stdin.readline().strip().split())
    if ch == 0:
        if find_parent(a) == find_parent(b):
            continue
        parent[find_parent(b)] = parent[find_parent(a)] # *
        # parent[b] = parnet[a] XX
    else:
        if find_parent(a) == find_parent(b):
            print('yes')
        else:
            print('no')
