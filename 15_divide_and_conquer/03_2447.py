# 별찍기
import sys
import math

def get_stars(n):
    starts = []
    for i in range(3 * len(n)):
        # n(즉 len(stars))이 3으로 나누어 떨어지지 않는다면(1이 남는다면) 가운데 공백을 줌(n의 길이 만큼)
        if i // len(n) ==  1:
            starts.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        # n이 3으로 나누어 떨어진다면, 공백 없이 가득 채움
        else:
            starts.append(n[i % len(n)] * 3)
    return starts

n = int(sys.stdin.readline().strip())
stars_basic = ["***", "* *", "***"]
k = int(math.log(n, 3)) - 1

for i in range(k):
    stars = get_stars(stars_basic)
for i in stars:
    print(i)