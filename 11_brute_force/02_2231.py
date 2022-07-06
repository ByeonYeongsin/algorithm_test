# 분해합
import sys

N = int(sys.stdin.readline().strip())
desum = 0
for i in range(1, N+1):
    list_i = list(map(int, str(i)))
    desum = i + sum(list_i)
    if desum == N:
        print(i)
        break
    if i == N:
        print(0)
