# 농작물 수확하기

import sys

f = open("00_input.txt", 'r')
T = int(f.readline().strip())
for t in range(T):
    n = int(f.readline().strip())
    sum = 0
    for i in range(n):
        rows=[]
        row_str = f.readline().strip()
        for now_str in row_str:
            rows.append(int(now_str))
        if i > n//2:
            c = n-i
        else:
            c = i+1
        for num in range(int(n/2-(2*c-1)/2), int(n/2+(2*c-1)/2)):
            sum += rows[num]    
    print('#', t+1, ' ', sum, sep='')