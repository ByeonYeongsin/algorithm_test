# 222-풀링

import sys

N = int(sys.stdin.readline().strip())
nums = []
for i in range(N):
    tmp=list(map(int, input().split()))
    nums.append(tmp)

def pooling(nums, n):
    if n == 1:
        return nums[0][0]
    new_map = [[] for _ in range(n//2)]
    
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            # now_pool = []
            # now_pool.append(nums[i][j])
            # now_pool.append(nums[i][j+1])
            # now_pool.append(nums[i+1][j])
            # now_pool.append(nums[i+1][j+1])
            # now_pool.sort()
            now_pool = [nums[i][j], nums[i][j+1], nums[i+1][j], nums[i+1][j+1]]
            now_pool.sort()
            new_map[i//2].append(now_pool[2])
    return pooling(new_map, n//2)

print(pooling(nums, N))
