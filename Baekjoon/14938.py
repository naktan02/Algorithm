import heapq
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
items = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

max_score = 0
for i in range(1,n+1):
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue,(0,i))
    c_max_score = 0
    check = [0]*(n+1)
    while queue:
        ccost,cnode = heapq.heappop(queue)
        if check[cnode] == 1:
            continue
        check[cnode] = 1    
        c_max_score += items[cnode-1]
        for fnode, fcost in graph[cnode]:
            if ccost + fcost > m:
                continue
            if check[fnode] == 1:
                continue
            heapq.heappush(queue,(ccost+fcost,fnode))
    max_score = max(max_score,c_max_score)

print(max_score)



