# 출석체크
import sys

N, K, Q, M = map(int, sys.stdin.readline().strip().split())
k_nums = list(map(int, sys.stdin.readline().strip().split()))
q_nums = list(map(int, sys.stdin.readline().strip().split()))

attendances = [0] * (N+3)

for i in range(1, N+3):
    for j in q_nums:
        if i % j == 0:
            attendances[i] = 1
            break
for k in k_nums:
    attendances[k] = 0 

for i in range(M):
    S, E = map(int, sys.stdin.readline().strip().split())
    print((E+1-S) - sum(attendances[S:E+1]))
