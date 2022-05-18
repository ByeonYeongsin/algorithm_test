# view
import sys

f = open("input/0_input.txt", 'r')
T = 1
for step in range(T):
    sum = 0
    n = int(f.readline().strip())
    num_list = list(map(int, f.readline().strip().split()))
    n1, n2, n3, n4, n5 = num_list[0], num_list[1], num_list[2], num_list[3], num_list[4]
    for i in range(4, n-2):
        now_height = n3 - max(n1, n2, n4, n5)
        if now_height > 0:
            sum += now_height
        n1, n2, n3, n4 = n2, n3, n4, n5
        n5 = num_list[i+1]
    print('#', step+1, ' ', sum, sep='')
f.close()

for l in range(1, 11):
    r = int(input())
    b = list(map(int, input().split()))
    c = 0
    #왼쪽2칸과 오른쪽 2칸은 비어있음
    for i in range(2, r-2):
        #왼쪽과 오른쪽 빌딩중에서 제일 빌딩을 찾음
        m = max(b[i+1], b[i+2], b[i-1], b[i-2])
        # 현재 빌딩과 제일큰빌딩을 비교할때 현재빌딩보다 작다면 차 만큼 결과에 더해주기
        if b[i] - m > 0 : c += b[i] - m
    print("#{} {}".format(l, c))