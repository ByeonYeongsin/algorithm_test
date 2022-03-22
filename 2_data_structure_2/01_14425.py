# 문자열집합

import sys

N, M = map(int, sys.stdin.readline().split())
str_set = set()

for i in range(N):
    now_str = sys.stdin.readline().strip()
    str_set.add(now_str)

count = 0

for j in range(M):
    now_check_str = sys.stdin.readline().strip()
    if now_check_str in str_set:
        count += 1

print(count)