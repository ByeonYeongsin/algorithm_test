# 블로그

import sys

n, x = map(int, sys.stdin.readline().strip().split())
vis_list = list(map(int, sys.stdin.readline().strip().split()))

# max_count = 0
# now = 0
# for i in range(0, x):
#     now += vis_list[i]

# if max(vis_list) == 0:
#     print('SAD')
# else:
#     for i in range(1, len(vis_list)-x+1):
#         if vis_list[i-1] == vis_list[i+x-1]:
#             max_count += 1
#         elif vis_list[i-1] < vis_list[i+x-1]:
#             now -= vis_list[i-1]
#             now += vis_list[i+x-1]
#             max_count = 1

#     print(now)
#     print(max_count)

input = sys.stdin.readline
N, X = map(int, input().split())
data = list(map(int, input().split()))

if max(data) == 0:
    print("SAD")
else:
    value = sum(data[:X])

    max_value = value
    max_cnt = 1

    for i in range(X, N):
        value += data[i]
        value -= data[i-X]

        if value > max_value:
            max_value = value
            max_cnt = 1
        
        elif value == max_value:
            max_cnt += 1
    print(max_value)
    print(max_cnt)