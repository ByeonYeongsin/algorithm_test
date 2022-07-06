# 줄세우기
import sys

N = int(sys.stdin.readline().strip())
students = [0] * N
for i in range(N):
    students[i] = int(sys.stdin.readline().strip())

# n - 증가하는 가장 긴 부분 수열
dp = [1] * N
for i in range(N):
    for j in range(i):
        if students[j] < students[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N-map(dp))
