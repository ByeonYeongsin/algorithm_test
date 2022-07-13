# 나무 자르기

import sys

def binarysearch(trees, M, start, end):
    mid = (start + end) // 2
    tmp = 0
    for tree in trees:
        if tree > mid:
            tmp += (tree-mid)
    if tmp == M:
        return mid
    if tmp < M:
        return binarysearch(trees, M, start, mid-1)
    if tmp > M:
        return binarysearch(trees, M, mid+1, end)

N, M = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

print(binarysearch(trees, M, 0, max(trees)))