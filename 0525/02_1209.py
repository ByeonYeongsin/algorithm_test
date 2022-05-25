# 2일차 - Sum

import sys

f = open("C:/algorithm_test/0525/02_input.txt", 'r')
for _ in range(10):
    t = int(f.readline().strip())
    nums = []
    for _ in range(100):
        nums.append(list(map(int, f.readline().strip().split())))

    max_sum = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += nums[i][j]
            col_sum += nums[j][i]
        if row_sum > max_sum:
            max_sum = row_sum
        if col_sum > max_sum:
            max_sum = col_sum
    
    stride_sum_right = 0
    stride_sum_left = 0
    for i in range(100):
        stride_sum_right += nums[i][i]
        stride_sum_left += nums[9-i][9-i]
    if stride_sum_left > max_sum:
        max_sum = stride_sum_left
    if stride_sum_right > max_sum:
        max_sum = stride_sum_right

    print('#', t, ' ', max_sum, sep='')     