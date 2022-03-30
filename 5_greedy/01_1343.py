# 폴리오미노

import sys

board = sys.stdin.readline().strip().replace('XXXX', 'AAAA').replace('XX', 'BB')
if 'X' in board:
    print(-1)
else:
    print(board)

str = "Aaaa"
str.replace("A", "b")
print(str)
print("Aaaa".replace("A", "c"))