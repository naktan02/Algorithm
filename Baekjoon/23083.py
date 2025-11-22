import sys


input = sys.stdin.readline
n,m = map(int,input().split())
tile = [[0]*(m+2) for _ in range(n+2)]
k = int(input())
for _ in range(k):
    y,x = map(int,input().split())
    tile[y][x] = -1


tile[1][1] = 1
for j in range(1,m+1):
    for i in range(1,n+1):
        if tile[i][j] == -1:
            continue
        if j %2 == 1:
            if tile[i-1][j] != -1 and i-1 >=0:
                tile[i][j] += tile[i-1][j]
            if tile[i][j-1] != -1 and j-1 >=0:
                tile[i][j] += tile[i][j-1]
            if tile[i-1][j-1] != -1 and j-1 >=0:
                tile[i][j] += tile[i-1][j-1]
        else:
            if tile[i-1][j] != -1 and i-1 >=0:
                tile[i][j] += tile[i-1][j]
            if tile[i+1][j-1] != -1 and j-1 >=0:
                tile[i][j] += tile[i+1][j-1]
            if tile[i][j-1] != -1 and j-1 >=0:
                tile[i][j] += tile[i][j-1]
print(tile[n][m] % 1000000007)



    
    