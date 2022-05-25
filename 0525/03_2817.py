# 부분 수열의 합

import sys

def dp(curr_index, curr_sum):
    global count
    global nums
    global N
    global K

    new_sum = curr_sum + nums[curr_index]
    if new_sum == K:
        count+=1
        # return XXXXX
    if curr_index == N-1:
        return
    if new_sum > K:
        return
    
    dp(curr_index+1, new_sum)
    dp(curr_index+1, curr_sum)

f = open("C:/algorithm_test/0525/03_input.txt", 'r')
T = int(f.readline().strip())
for t in range(T):
    N, K = map(int, f.readline().strip().split())
    nums = list(map(int, f.readline().strip().split()))

    count = 0
    dp(0, 0)
    print('#', t+1, ' ', count, sep='')