# 설탕 배달
# dp초기화 최소면 최대로, 최대면 최소로
# 2147000000

import sys
import math

N = int(sys.stdin.readline().strip())
dp = [-1] * (N+7)
dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    if (dp[i-3] > 0) and (dp[i-5] > 0):
        dp[i] = min(dp[i-3], dp[i-5]) + 1
    elif dp[i-3] > 0:
        dp[i] = dp[i-3] + 1
    elif dp[i-5] > 0:
        dp[i] = dp[i-5] + 1

if 0 < dp[N]:
    print(dp[N])
else:
    print(-1)

# 나누기로 푸는 법

num = int(input())
count = 0

while num >= 0:
  if num % 5 == 0:
    count += int(num // 5)
    print(count)
    break
  
  num -= 3
  count += 1
  
else:
  print(-1)