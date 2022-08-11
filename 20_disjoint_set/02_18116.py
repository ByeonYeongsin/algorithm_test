# 로봇 조립
import sys

N = int(sys.stdin.readline().strip())
robots = [-1 for i in range(1000000 + 1)]

def find(x):
    if robots[x] < 0:
        return x
    else:
        y = find(robots[x])
        robots[x] = y
        return y

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if robots[x] < robots[y]:
        A, B = x, y
    else:
        A, B = y, x

    robots[A] += robots[B]
    robots[B] = A

for _ in range(N):
    li = list(map(str, input().split()))
    if li[0] == "I":
        a = int(li[1])
        b = int(li[2])
        union(a, b)

    if li[0] == "Q":
        a = int(li[1])
        print(robots[find(a)] * - 1)
