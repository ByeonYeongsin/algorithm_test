# 돌 게임

import sys

n = int(sys.stdin.readline().strip())
now = 1

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2
dp[3] = 1
for i in range(4, n+1):
    dp[i] = dp[i-2] 
 
if dp[n] == 1:
    print('SK')
else:
    print('CY')