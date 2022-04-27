# # 2차원 배열의 합

# import sys

# N, M = map(int, sys.stdin.readline().strip().split())
# arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# k = int(sys.stdin.readline().strip())
# for _ in range(k):
#     sum = 0
#     i, j , x, y = map(int, sys.stdin.readline().strip().split())
#     for row in range(i-1, y):
#         for col in range(j-1, y):
#             sum += arr[row][col]
#     print(sum)

import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * (m+1) for _ in range(n+1)]
 
for i in range(1, n+1):
    for j in range(1, m+1):
        memo[i][j] = arr[i-1][j-1] + memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1]
 
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[i-1][y] - memo[x][j-1] + memo[i-1][j-1])