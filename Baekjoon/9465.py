import sys
t=int(sys.stdin.readline())
for _ in range(t):
    n = int(input())
    data = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    for i in range(1,n):
        if i == 1:
            data[0][i] = data[1][0] + data[0][i]
            data[1][i] = data[0][0] + data[1][i]
            continue
        data[0][i] = data[0][i] + max(data[1][i-1],data[1][i-2])
        data[1][i] = data[1][i] + max(data[0][i-1],data[0][i-2])
    print(max(data[0][n-1],data[1][n-1]))