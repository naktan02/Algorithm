import sys
import heapq

n,m = map(int,sys.stdin.readline().split())
nodes = [list() for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    nodes[a].append((c,b))

K = 3
dist = [[100000]*K for _ in range(n+1)]
dist[1][0] = 0
visited = set(map(int,sys.stdin.readline().split()))
queue = []
start = 1 if 1 in visited else 0
heapq.heapify(queue)
heapq.heappush(queue,(0,1,start))
check = True
while queue:
    a,b,c= heapq.heappop(queue)
    if a != dist[b][c]:
        continue
    if b == n:
        if c == 2:
            print(a)
            check = False
            break
        else:
            continue
    for node in nodes[b]:
        temp = 0
        q,w = node
        if b == w:
            continue
        if w in visited:
            temp = 1
        if a+q < dist[w][c+temp]:
            dist[w][c+temp] = a+q
            heapq.heappush(queue,(a+q,w,c+temp))

if check:
    print(-1)