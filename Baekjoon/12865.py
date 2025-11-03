import sys
n,k = map(int,sys.stdin.readline().split())
weight = []
value = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    weight.append(a)
    value.append(b)

#2차원
def two():
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,k+1):
            if weight[i-1] <= j:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i-1]] + value[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][k])


## 1차원
def one():
    dp = [0] * (k+1)
    for i in range(1,n+1):
        for limit in range(k,0,-1):
            if limit >= weight[i-1]:
                dp[limit] = max(dp[limit], dp[limit-weight[i-1]] + value[i-1])
    print(dp[k])
one()
