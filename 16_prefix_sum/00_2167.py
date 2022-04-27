# 2차원 배열의 합

import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

k = int(sys.stdin.readline().strip())
for _ in range(k):
    sum = 0
    i, j , x, y = map(int, sys.stdin.readline().strip().split())
    for row in range(i-1, y):
        for col in range(j-1, y):
            sum += arr[row][col]
    print(sum)
