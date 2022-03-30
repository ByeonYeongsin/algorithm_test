# 주지수

import sys

# insert 주의
# a = [1, 2, 3]
# a.insert(0, 4)
# print(a)
# print([1, 2, 3].insert(0, 4))




N, M = map(int, sys.stdin.readline().strip().split())
size = [[0 for col in range(M+1)] for row in range(N+1)]
dp = [[0 for col in range(M+1)] for row in range(N+1)]

for i in range(1, N+1):
    size[i] = list(map(int, sys.stdin.readline().strip().split()))
    size[i].insert(0, 0)


for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + size[i][j]

k = int(sys.stdin.readline().strip())

for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][x2-1])