# 폴리오미노

import sys

board = sys.stdin.readline().strip()
board_x = list(filter(None, board.split('.')))
board_dot = list(filter(None, board.split('X')))

poly = ''
poly_a = 'AAAA'
poly_b = 'BB'

for str in board_x:
    if len(str) % 2 != 0:
        poly = '-1'
        break
else:
    if board[0] == '.': 
        poly += board_dot
        board_dot.remove(0)
    for i in range(len(board_x)): 
        poly += poly_a * (len(board_x[i]) // 4)
        poly += poly_b * ((len(board_x[i]) % 4) // 2)
        if len(board_dot) >= i+1:
            poly += board_dot[i]

print(poly)