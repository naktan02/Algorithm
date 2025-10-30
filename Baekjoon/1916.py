import sys
from heapq import heappush, heappop
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
data = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    data[a].append([b,c])
start, end = map(int,sys.stdin.readline().split())
INF = 10**18
dist = [INF]*(n+1)
dist[start] = 0
pq = []
heappush(pq, (0, start))
while pq:
    cost,u = heappop(pq)
    if dist[u] < cost:
        continue
    if u == end:
        break
    for s,c in data[u]:
        c+=cost
        if dist[s] > c:
            dist[s] = c
            heappush(pq,(c,s))
print(dist[end])