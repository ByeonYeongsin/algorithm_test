# 배열 합치기

import sys

n, m = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))
m_list = list(map(int, sys.stdin.readline().strip().split()))
num_list = num_list + m_list

for i in range(1, len(num_list)):
    now_num = num_list[i]
    for j in range(i-1, -1, -1):
        if now_num < num_list[j]:
            num_list[j+1], num_list[j] = num_list[j], now_num
        else:
            break

print(*num_list)