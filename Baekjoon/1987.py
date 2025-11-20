n,m = map(int,input().split())
data = [list(input()) for _ in range(n)]
add = [(1,0),(-1,0),(0,1),(0,-1)]

visited = [0]*26
result = 0
def back(y,x,cnt):
    global result
    if result < cnt:
        result = cnt
    for t_y,t_x in add:
        r_y = y + t_y
        r_x = x + t_x
        if 0 <= r_x < m and 0 <= r_y < n:
            idx = ord(data[r_y][r_x]) - ord("A")
            if visited[idx] == 0:
                visited[idx] = 1
                back(r_y,r_x,cnt+1)
                visited[idx] = 0

idx = ord(data[0][0]) - ord("A")
visited[idx] = 1
back(0,0,1)
print(result)