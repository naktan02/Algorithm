from collections import deque
n,m = map(int,input().split())
lab = [list(map(int,input().split())) for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]
max_count = 0

def bfs(labs):
    queue = deque()
    for y in range(n):
        for x in range(m):
            if labs[y][x] == 2:
                queue.append((y,x))
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < m:
                if labs[ny][nx] == 0:
                    labs[ny][nx] = 2
                    queue.append((ny,nx))
    count = 0
    for y in range(n):
        for x in range(m):
            if labs[y][x] == 0:
                count += 1

    
    return count

def back(y,x,count):
    global max_count
    if count == 3:
        copied = [row[:] for row in lab]
        temp_count = bfs(copied)
        max_count = max(max_count,temp_count)
        return
    for i in range(y,n):
        for j in range(x if i == y else 0,m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                back(i,j,count+1)
                lab[i][j] = 0
back(0,0,0)
print(max_count)