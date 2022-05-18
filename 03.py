# N-Queen

import sys

def queen(row, col):
    global board
    global N
    global count
    for i in range(N):
        if board[row][i] == 1:
            return
        if board[i][col] == 1:
            return
    for i in range(1, min(row, col)+1):
        if board[row-i][col-i] == 1:
            return
    board[row][col] = 1
    if row == N-1:
        count += 1


f = open('input/3_input.txt', 'r')
T = int(f.readline().strip())

for t in range(T):
    count = 0
    N = int(f.readline().strip())
    for row in range(N):
        board = [[0] * N for _ in range(N)]
        for col in range(N):
            print(row, col)
            queen(row, col)
    print('#', t, ' ', count, sep='')
f.close()
