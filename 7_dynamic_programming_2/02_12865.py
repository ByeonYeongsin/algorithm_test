# 평범한 배낭
from _typeshed import StrPath
import sys

weight = []
value = []
dp = []

n, k = map(int, sys.stdin.readline().strip().split())
for i in range(n):
    w, v = map(int, sys.stdin.readline().strip().split())
    weight.append(w)
    value.append(v)
