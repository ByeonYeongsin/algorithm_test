# 공약수

import sys

num_list = []
N = int(sys.stdin.readline().strip())
num_list = map(int, sys.stdin.readline().strip().split())

for i in range(1, max(num_list)):
    for num in num_list:
        if num % i != 0:
            break
    else:
        print(i)
        print()