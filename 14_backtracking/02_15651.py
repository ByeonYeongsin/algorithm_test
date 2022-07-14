# N과 M(3)

import sys

N, M = map(int, sys.stdin.readline().strip().split())
s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    else:
        for i in range(1, N+1):
            s.append(i)
            dfs()
            s.pop()
dfs()