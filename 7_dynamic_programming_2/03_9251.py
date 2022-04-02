# LCS
# Not Yet

import sys
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

count = 0
n2 = 0

for i in str1:
    now_n2 = n2
    for j in range(n2, len(str2)):
        if i == str2[j]:
            count += 1
print(max)