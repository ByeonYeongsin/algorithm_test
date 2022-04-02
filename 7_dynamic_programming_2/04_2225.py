# 합분해
# Not Yet

import sys

n, k = map(int, sys.stdin.readline().strip().split())
dp = [[0] * (k+1) for _ in range (n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j == 1:
            dp[i][j] = 1
        elif i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp)
print(dp[n][k])