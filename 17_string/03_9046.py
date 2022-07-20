# 복호화
import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    str = sys.stdin.readline().strip().replace(" ", "").split()
    str = str[0]
    nums = [0]*26
    for s in str:
        if s.isalpha():
            nums[ord(s)-ord('a')] += 1
    max_num = max(nums)
    if nums.count(max_num) < 2:
        print(chr(ord('a') + nums.index(max_num)))
    else:
        print('?')