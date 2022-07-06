# 겹치는건 싫어
import sys

# N, K = map(int, sys.stdin.readline().strip().split())
# arr = list(map(int, sys.stdin.readline().strip().split()))
# mcns = [1] * N

# for i in range(N):
#     if N-i <= max(mcns):
#         break
#     overlap = {}
#     overlap[arr[i]] = 1
#     for j in range(i+1, N):
#         if arr[j] in overlap:
#             overlap[arr[j]] += 1
#             if overlap[arr[j]] > K:
#                 break
#         else:
#             overlap[arr[j]] = 1
#         mcns[i] += 1    
# print(max(mcns))

N, K = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))
left, right = 0, 0

counter = [0] * (max(numbers) + 1)
answer = 0
while right < N:
    if counter[numbers[right]] < K:
        counter[numbers[right]] += 1
        right += 1
    else:
        counter[numbers[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)