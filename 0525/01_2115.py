# 3일차 - 회문1

from pickle import FALSE
import sys
f = open("C:/algorithm_test/0525/01_input.txt", 'r')
for t in range(10):
    renum = int(f.readline().strip())
    board = [] 
    for _ in range(8):
        board.append(list(f.readline().strip()))
    count = 0
    for row in range(8):
        for col in range(0, 8-renum+1):
            renum_flag = True
            for n in range(renum//2):           
                if board[row][col+n] != board[row][col+renum-1-n]:
                    renum_flag = False
                    break
            if renum_flag == True:
                count += 1

    for row in range(8-renum+1):
        for col in range(0, 8):
            renum_flag = True
            for n in range(renum//2):
                if board[row+n][col] != board[row+renum-1-n][col]:
                    renum_flag = False
                    break
            if renum_flag == True:
                count += 1
    print('#', t+1, ' ', count, sep='')     