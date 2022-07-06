# 효율적인 해킹
import sys

def dfs(start, confi, hack_num):
    for now_com in confi[start]:
        dfs(now_com, confi, hack_num)
        hack_num[start] += hack_num[now_com]
    

N, M = map(int, sys.stdin.readline().strip().split())
confi = [[] for _ in range(N+1)]
hack_num = [1] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    confi[a].append(b)

for i in range(1, N+1):
    dfs(i, confi, hack_num)

print(hack_num)