# 스택 수열
import sys

n = int(sys.stdin.readline().strip())
tmp = 1
stack = []
answer = []

for _ in range(n):
    now_num = int(sys.stdin.readline().strip())
    while tmp <= now_num:
        stack.append[tmp]
        answer.append('+')
        tmp += 1

    if stack[-1] == now_num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
