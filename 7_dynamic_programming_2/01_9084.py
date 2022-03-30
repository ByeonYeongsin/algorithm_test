# 동전

import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    c_list = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())

    dp = [0 for i in range(m + 1)]
    dp[0] = 1
    for i in c_list:
        for j in range(1, m + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    print(dp[m])