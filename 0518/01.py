# 최대 상금
#경우의 수 찾기, 매개변수로 몇번 바꿧는지 적는다.
def dfs(count):
    global answer
    if count == 0:
        tmp = int(''.join(num))
        if answer < tmp:
            answer = tmp
        return
    else:
        for i in range(leng):
            for j in range(i+1, leng):
                num[i], num[j] = num[j], num[i]
                temp_key = ''.join(num)
                if (temp_key, count-1) not in visited:
                    visited.append((temp_key, count-1))
                    dfs(count-1)
                num[i], num[j] = num[j], num[i]
    
f = open("input/1_input.txt", 'r')
for i in range(int(f.readline().strip())):
    num, count = map(int, f.readline().strip().split())
    num = list(str(num))
    count = int(count)
    leng = len(num)
    visited = []
    answer = -1
    dfs(count)
    print('#{} {}'.format(i+1, answer))