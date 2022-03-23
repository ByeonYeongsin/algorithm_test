# 피로도
import sys

a, b, c, m = map(int, sys.stdin.readline().strip().split())
now_m = 0
w_hour = 0

for _ in range(1, 25):
    if now_m + a <= m:
        w_hour += 1
        now_m += a
    else:
        now_m -= c
        if now_m < 0:
            now_m = 0

print(b * w_hour)