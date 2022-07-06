# 가장 긴 짝수 연속한 부분 수열 (large)
import sys
from turtle import right

N, K = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
ans = 0
first, last = 0, 0
odd_count = arr[first] % 2

while last < N:
    if odd_count <= K:
        last += 1
        odd_count += arr[last] % 2
    if odd_count > K:
        first += 1
        odd_count -= arr[first-1] % 2
    ans = max(ans, last-first+1-odd_count)

print(ans)

