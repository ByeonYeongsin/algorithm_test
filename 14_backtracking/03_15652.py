# N과 M(4)

import sys

N, M = map(int, sys.stdin.readline().strip().split())
s = []

def dfs(now):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    else:
        for i in range(now, N+1):
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)