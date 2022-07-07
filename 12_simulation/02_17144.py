# 미세먼지 안녕!
import sys

# 미세먼지 이동
def dust_move():
    temp = [[0] * C for _ in range(R)]  # 확산값 저장
    for i in range(R):
        for j in range(C):
            if air[i][j] >= 5:
                val = 0  # 얼마나 확산했는지
                # 상
                if i - 1 >= 0 and air[i - 1][j] != -1:
                    temp[i - 1][j] += air[i][j] // 5
                    val += air[i][j] // 5
                # 하
                if i + 1 < R and air[i + 1][j] != -1:
                    temp[i + 1][j] += air[i][j] // 5
                    val += air[i][j] // 5
                # 좌
                if j - 1 >= 0 and air[i][j - 1] != -1:
                    temp[i][j - 1] += air[i][j] // 5
                    val += air[i][j] // 5
                # 우
                if j + 1 < C and air[i][j + 1] != -1:
                    temp[i][j + 1] += air[i][j] // 5
                    val += air[i][j] // 5
                temp[i][j] -= val  # 확산값 빼기
    for i in range(R):
        for j in range(C):
            air[i][j] += temp[i][j]  # 확산받은 값 더하기


def air_move():
    # up
    # 1 - 아래
    temp = air[up[0]][C - 1]
    for i in range(C - 1, 1, - 1):
        air[up[0]][i] = air[up[0]][i - 1]
    air[up[0]][1] = 0

    # 2 - 오른쪽
    temp_1 = air[0][C - 1]
    for i in range(up[0] - 1):
        air[i][C - 1] = air[i + 1][C - 1]
    air[up[0] - 1][C - 1] = temp

    # 3 - 위쪽
    temp_2 = air[0][0]
    for i in range(C - 2):
        air[0][i] = air[0][i + 1]
    air[0][C - 2] = temp_1

    # 4 - 왼쪽
    for i in range(up[0] - 1, 1, -1):
        air[i][0] = air[i - 1][0]
    air[1][0] = temp_2

    # down
    # 1- 위쪽
    temp = air[down[0]][C - 1]
    for i in range(C - 1, 1, -1):
        air[down[0]][i] = air[down[0]][i - 1]
    air[down[0]][1] = 0

    # 2 오른쪽
    temp_1 = air[R - 1][C - 1]
    for i in range(R - 1, down[0] + 1, -1):
        air[i][C - 1] = air[i - 1][C - 1]
    air[down[0] + 1][C - 1] = temp

    # 3 - 아래쪽
    temp_2 = air[R - 1][0]
    for i in range(C - 2):
        air[R - 1][i] = air[R - 1][i + 1]
    air[R - 1][C - 2] = temp_1

    # 4 - 왼쪽
    for i in range(down[0] + 1, R - 1):
        air[i][0] = air[i + 1][0]
    air[R - 2][0] = temp_2

R, C, T = map(int, sys.stdin.readline().strip().split())
air = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]

for i in range(R):
    if air[i][0] == -1:
        up, down = [i, 0], [i+1, 0]
        break

for i in range(T):
    dust_move()
    air_move()

total = 0
for i in range(R):
    for j in range(C):
        if air[i][j] > 0:
            total += air[i][j]

print(total)