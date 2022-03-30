# 피보나치수2

import sys

n = int(sys.stdin.readline().strip())
f = []
f.append(0)
f.append(1)

for i in range(2, n+1):
    f.append(f[i-1]+f[i-2])

print(f[n])