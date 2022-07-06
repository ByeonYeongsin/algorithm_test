# 수학은 비대면강의입니다
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().strip().split())
# y = int((d*c - a*f)/(d*b-a*e))
# x = int((c-b*y)/a)

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x+b*y==c) and (d*x+e*y==f):
            print(x, y)
            break

# print(x, y, sep=' ')