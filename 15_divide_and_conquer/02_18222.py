# 투에-모스 문자열
import sys
import math

def do_toemos(n, k):
    if n == 1:
        print(k) 
        return

    num = math.log(n, 2)
    if num-int(num) == 0: # 완벽히 나누어 떨어지는 경우
        if num % 2 == 0:
            print(k)
            return
        else:
            print((k+1)%2)
            return
    else:
        num = int(num)

    if num % 2 == 0:
        do_toemos(n-2**num, (k+1)%2)
    else:
        k = (k+1) % 2
        do_toemos(n-2**num, k)

k = int(sys.stdin.readline().strip())
do_toemos(k, 0)