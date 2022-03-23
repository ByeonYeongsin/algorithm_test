# 공약수
# 유클리드 호제법

import sys

def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)
    
num_list = []
N = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().strip().split()))
# list로 받을 시 list 반드시 씌워줘야함

gcd = num_list[0]
for i in range(1, N):
    gcd = GCD(gcd, num_list[i])

# 최대공약수로 공약수 구하기
outputs = []
x = 1
while x * x <= gcd:
    if gcd % x == 0:
        outputs.append(x)
        if x * x != gcd:
            outputs.append(gcd // x)
    x += 1

outputs.sort()
print(*outputs)