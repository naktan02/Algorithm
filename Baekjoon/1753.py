import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

start = int(input())
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance = [INF] * (n+1)
    queue = []
    distance[start] = 0

    heapq.heappush(queue,(0,start))
    while queue:
        cost,now = heapq.heappop(queue)
        if distance[now] < cost:
            continue
        for front, weight in graph[now]:
            c = cost + weight
            if c < distance[front]:
                distance[front] = c
                heapq.heappush(queue,(c,front))
    return distance

distance = dijkstra(start)
for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)

