# N과 M (2)

import sys

n, m = map(int, sys.stdin.readline().strip().split())

s = []

def dfs(now):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(now, n+1):
        if i not in s:
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)
