import sys
n = int(sys.stdin.readline())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
max_result = [[0,0,0] for _ in range(n)]

max_result[0] = data[0]
for i in range(1,len(data)):
    for j in range(3):
        temp = data[i][j]
        if j == 0:
            max_result[i][j] = temp + max(max_result[i-1][0],max_result[i-1][1])
            data[i][j] = data[i][j] + min(data[i-1][0],data[i-1][1])
        elif j == 1:
            max_result[i][j] = temp + max(max_result[i-1][0],max_result[i-1][1],max_result[i-1][2])
            data[i][j] = data[i][j] + min(data[i-1][0],data[i-1][1],data[i-1][2])
        else:
            max_result[i][j] = temp + max(max_result[i-1][1],max_result[i-1][2])
            data[i][j] = data[i][j] + min(data[i-1][1],data[i-1][2])

print(max(max_result[-1]),min(data[-1]))
        
        
