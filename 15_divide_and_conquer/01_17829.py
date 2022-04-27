# 222-풀링

import sys

N = int(sys.stdin.readline().strip())
map = [list(map(int, sys.stdin.readline().strip().split()) for _ in range(N))]

def pooling(map, n):
    if n == 1:
        return map[0][0]
    new_map = [[] for _ in range(n//2)]
    
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            new_map[i//2].append(sorted([map[i][j], map[i][j+1], map[i+1][j], map[i+1][j+1]])[2])
    return pooling(new_map, n//2)

print(pooling(map, N))
