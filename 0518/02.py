# Flatten

import sys

f = open("input/2_input.txt", 'r')
for i in range(10):
    count = int(f.readline().strip())
    nums = list(map(int, f.readline().strip().split()))
    for _ in range(count):
        nums[nums.index(max(nums))] -= 1
        nums[nums.index(min(nums))] += 1

    print('#', i+1, ' ',max(nums) - min(nums), sep='')    