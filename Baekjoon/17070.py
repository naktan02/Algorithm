n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
w = [[0]*(n+1) for _ in range(n+1)]
h = [[0]*(n+1) for _ in range(n+1)]
d = [[0]*(n+1) for _ in range(n+1)]
w[1][2] = 1
for i in range(1,n+1):
    for j in range(3,n+1):
        if data[i-1][j-1] != 1:
            w[i][j] = w[i][j-1] + d[i][j-1]
            h[i][j] = h[i-1][j] + d[i-1][j]
        if data[i-2][j-1] != 1 and data[i-1][j-2] != 1 and data[i-1][j-1] !=1:
            d[i][j] = w[i-1][j-1] + h[i-1][j-1] + d[i-1][j-1]
print(w[n][n]+h[n][n]+d[n][n])

