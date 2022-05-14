# 네트워크 연결
from heapq import heappop, heappush
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

def prim(start, weight) :
    visit=[0]*(n+1)     # 정점 방문 처리
    q=[[weight, start]]     # 힙 구조를 사용하기 위해 가중치를 앞에 둠
    ans=0   # 가중치 합
    cnt=0   # 간선의 개수
    while cnt < n :     # 간선의 개수 최대는 V-1
        k, v=heappop(q)
        if visit[v] : 
            continue # 이미 방문한 정점이면 지나감
        visit[v]=1      # 방문안했으면 방문처리
        ans+=k      # 해당 정점까지의 가중치를 더해줌
        cnt+=1      # 간선의 갯수 더해줌
        for u, w in G[v] :  # 해당 정점의 간선정보를 불러옴
            heappush(q, [w, u])     # 힙에 넣어줌
    return ans

G=[[] for _ in range(n+1)]
for _ in range(m) :
    u, v, w=map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

print(prim(1, 0))
