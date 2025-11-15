import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize

def dijkstra(start_node):

    distance = [INF] * (N + 1)
    
    pq = []
    
    heapq.heappush(pq, (0, start_node))
    distance[start_node] = 0
    
    while pq:
        dist, now = heapq.heappop(pq)
        
        if distance[now] < dist:
            continue
            
        for neighbor, weight in graph[now]:
            cost = dist + weight
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(pq, (cost, neighbor))
                
    return distance


N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]

path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

result = min(path1, path2)

if result >= INF:
    print(-1)
else:
    print(result)