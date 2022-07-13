# 숫자 카드

import sys

def binarysearch(n_nums, key, start, end):
    if start > end:
        return 0
    else:
        mid = (start+end)//2
        if n_nums[mid] == key:
            return 1
        elif n_nums[mid] < key:
            return binarysearch(n_nums, key, mid+1, end)
        elif n_nums[mid] > key:
            return binarysearch(n_nums, key, start, mid-1)


N = int(sys.stdin.readline().strip())
n_nums = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())
m_nums = list(map(int, sys.stdin.readline().strip().split()))

n_nums.sort()

for now_m in m_nums:
    print(binarysearch(n_nums, now_m, 0, len(n_nums)-1), end=' ')