# 배열 합치기

import sys

n, m = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))
m_list = list(map(int, sys.stdin.readline().strip().split()))
num_list = num_list + m_list

# 버블 정렬 시간복잡도가 sort()보다 큼?
# for i in range(1, len(num_list)):
#     now_num = num_list[i]
#     for j in range(i-1, -1, -1):
#         if now_num < num_list[j]:
#             num_list[j+1], num_list[j] = num_list[j], now_num
#         else:
#             break

num_list.sort()

print(*num_list)