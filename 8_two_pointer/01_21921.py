# 블로그

import sys

n, x = map(int, sys.stdin.readline().strip().split())
vis_list = list(map(int, sys.stdin.readline().strip().split()))

max_count = 0
now = 0
for i in range(0, x):
    now += vis_list[i]

if max(vis_list) == 0:
    print('SAD')
else:
    for i in range(1, len(vis_list)-x+1):
        if vis_list[i-1] == vis_list[i+x-1]:
            max_count += 1
        elif vis_list[i-1] < vis_list[i+x-1]:
            now -= vis_list[i-1]
            now += vis_list[i+x-1]
            max_count = 1

    print(now)
    print(max_count)