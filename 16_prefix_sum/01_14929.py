# 귀찮아 (SIB)

import sys

# (xaxb) = x1x2 + x1x3 + ... + x(n-1)xn = x1(x2+x3+...+xn) + x2(x3+x4+...+xn) + xn-1(xn)

n = int(sys.stdin.readline().strip())
temp = list(map(int, sys.stdin.readline().strip().split()))
num = []
num.append(temp[0])

for i in range(1, n):
    num.append(num[i-1] + temp[i]) # x1, x1+x2, x1+x2+x3, ...

answer = 0
for i in range(n):
    answer += temp[i] * (num[n-1] - num[i]) # x1(x2+x3) + x2(x3)

print(answer)