n,m = map(int,input().split())
home = []
chicken = []
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        if temp[j] == 1:
            home.append([i+1,j+1])
        elif temp[j] == 2:
            chicken.append([i+1,j+1])

max_home = len(home)
max_chicken = len(chicken)
dist = [[0]*max_chicken for _ in range(max_home)]

for i in range(max_home):
    for j in range(max_chicken):
        dist[i][j] = abs(home[i][0]-chicken[j][0]) + abs(home[i][1]-chicken[j][1])

result = [10000] * max_home
def back(deep,best,start):
    if deep == m:
        if sum(result) < best:
            best = sum(result)
        return best
    for j in range(start,max_chicken):
        pre = result[:]
        for i in range(max_home):
            if result[i] > dist[i][j]:
                result[i] = dist[i][j]
        best = back(deep+1,best,j+1)
        result[:] = pre
    return best
best = back(0,100000,0)
print(best)
    