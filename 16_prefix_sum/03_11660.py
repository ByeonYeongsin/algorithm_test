# 구간 합 구하기 5
import sys

from numpy import matrix

N, M = map(int, sys.stdin.readline().strip().split())
nums = []
for _ in range(N):
    nums.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    for j in range(N):
        if j == 0:
            continue
        else:
            nums[i][j] += nums[i][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    answer = 0
    for i in range(x1-1, x2):
        if y1 != 1:
            answer -= nums[i][y1-1]
        answer += nums[i][y2-1]
    print(answer)