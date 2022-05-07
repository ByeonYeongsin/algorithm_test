# 집합의 표현
import sys

n, m = map(int, sys.stdin.readline().strip().split())
n_list = [0] * (n+1)

for i in range(m):
    ch, a, b = map(int, sys.stdin.readline().strip().split())
    if ch == 0:
        if a == b:
            continue
        if n_list[a] != 0:
            for j in range(len(n_list)):
                if n_list[b] == n_list[j] and n_list[j] != 0:
                    n_list[j] = n_list[a]
            n_list[b] = n_list[a]
        elif n_list[b] != 0:
            for j in range(len(n_list)):
                if n_list[a] == n_list[j] and n_list[j] != 0:
                    n_list[j] = n_list[b]
            n_list[a] = n_list[b]
        else:
            n_list[a] = n_list[b] = max(n_list) + 1
    else:
        if n_list[a] != 0 and n_list[b] != 0 and n_list[a] == n_list[b]:
            print('YES')
        else:
            print('NO')