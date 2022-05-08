# 문자열 집합

import sys

n, m = map(int, sys.stdin.readline().strip().split())

strings = [[] for _ in range(n)]

for i in range(n):
    strings[i] = sys.stdin.readline().strip()

ch = 0

for _ in range(m):
    now_str = sys.stdin.readline().strip()
    if now_str in strings:
        ch += 1
        
print(ch)

