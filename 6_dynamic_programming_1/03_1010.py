# 다리 놓기

import sys

# dp = [[0] * 31] * 31
# for west in range(1, 31):
#     for east in range(west, 31):
#         if west == 1:
#             dp[west][east] = east
#         if west == east:
#             dp[west][east] = 1


for west in range(2, 31):
    for east in range(west+1, 31):
        dp[west][east] = dp[west-1][east-1] + dp[west][east-1]

T = int(sys.stdin.readline().strip())
for i in range(T):
    west, east = map(int, sys.stdin.readline().strip().split())
    print(dp[west][east]) 