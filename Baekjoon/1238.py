import sys
import heapq
from collections import deque

input = sys.stdin.readline

n,m,x = map(int,input().split())

nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,t = map(int,input().split())
    nodes[a].append((b,t))

def dijkstra(start,end):
    if start == end:
        return 0
    queue = []
    heapq.heappush(queue,(0,start))
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        if now == end:
            break
        for next_node, time in nodes[now]:
            c = dist + time
            if c < distance[next_node]:
                distance[next_node] = c
                heapq.heappush(queue,(c,next_node))
    return distance[end]

ans = 0
for i in range(1,n+1):
    temp = dijkstra(i,x)
    temp += dijkstra(x,i)
    ans = max(ans,temp)
print(ans)



