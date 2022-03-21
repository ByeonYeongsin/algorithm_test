# 요세푸스 문제
# 1~N명 원, 양의 정수 K, 순서대로 K번째 사람 제거, 원에서 사람들이 제거되는 순서(N, K) - 요세푸스 순열
# ex) (7, 3) => <3, 6, 2, 7, 5, 1, 4>
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램

N, K = map(int, input().split())
n_list = list(range(1, N+1))
josephus_list = list()
now_index = K

while n_list:
    while now_index > len(n_list):
        now_index -= len(n_list)
        
    josephus_list.append(n_list.pop(now_index-1))
    now_index = now_index + K - 1


print(josephus_list)


# solution
from collections import deque

N, K = map(int, input().split())
josephus_list = []
q = deque(range(1, N+1)) # deque 기억

while len(q) != 0:
    q.rotate(-K) # 기억
    josephus_list.append(q.pop())
    
print('<' + ', '.join(map(str, josephus_list)) + '>') # 기억