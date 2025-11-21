import sys
from collections import deque

input = sys.stdin.readline
n,m,k = map(int,input().split())
tile = [[0]*m for _ in range(n)]
for _ in range(k):
    y,x = map(int,input().split())
    tile[y][x] = -1
holeport = [(0,1),(1,1),(-1,1),(1,0),(0,-1),(-1,0)]
evenport = [(0,1),(1,0),(-1,0),(1,-1),(0,-1),(-1,-1)]

queue = deque()
queue.append([0,0,0])
check = True
while queue:
    y,x,cnt = queue.popleft()
    if tile[y][x] == -1:
        continue
    tile[y][x] = -1
    if y == n-1 and x == m-1:
        print(cnt)
        check = False
        break
    if y%2 ==0:
        port = evenport
    else:
        port = holeport
    for ny,nx in port:
        ny +=y
        nx +=x
        if 0<=ny<n and 0<=nx<m and tile[ny][nx] != -1:
            queue.append([ny,nx,cnt+1])
if check:
    print(-1)
    
    
    