# 설탕 배달
# dp초기화 최소면 최대로, 최대면 최소로

import sys

N = int(sys.stdin.readline().strip())
dp = [99] * (N+7)
dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[N] < 99:
    print(dp[N])
else:
    print(-1)