# view
import sys

f = open("input/0_input.txt", 'r')
T = 10
for step in range(T):
    sum = 0
    n = int(f.readline().strip())
    nums = list(map(int, f.readline().strip().split()))
    for i in range(2, n-2):
        now_height = nums[i] - max(nums[i-1], nums[i-2], nums[i+1], nums[i+2])
        if now_height > 0:
            sum += now_height
    print('#', step+1, ' ', sum, sep='')
f.close()
