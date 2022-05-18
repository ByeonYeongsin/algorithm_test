n = int(input())
result = 0
graph = [0 for _ in range(n + 1)]

# 모든 퀸은 한 행에 한개씩 들어가기 때문에 행검사는 할 필요 없다
# 열 검사와 대각 검사만 하면 됨
# 위에서부터 차례로 내려오기 때문에 해당 row 전까지만 검사하면 된다

# 백트래킹을 위한 검사 함수
# col에는 가능한 col후보가 들어감
def promising(graph, row, col):
    # 열 검사
    for i in range(1, row):
        if graph[i] == col:
            return False
    # 대각 검사
    for i in range(1, row):
        if abs(graph[i] - col) == row - i:
            return False
    return True

def nqueen(graph, row, num):
    global result

    if row == num + 1:
        result += 1
        return

    # 1 ~ n 까지의 col 후보 중 가능 한 후보를 판별
    for col in range(1, n + 1):
        if promising(graph, row, col):
            graph[row] = col
            nqueen(graph, row + 1, num)
        else:
            continue

nqueen(graph, 1, n)
print(result)