# N과 M (1)

import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
