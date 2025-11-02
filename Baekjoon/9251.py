s = input()
t = input()
s_len = len(s)+1
t_len = len(t)+1
dp = [[0]*s_len for _ in range(t_len)]
for i in range(1,t_len):
    for j in range(1, s_len):
        if t[i-1] == s[j-1]:
            temp = 1
        else:
            temp = 0
        dp[i][j] = max(dp[i-1][j-1]+temp,dp[i-1][j],dp[i][j-1])
print(dp[t_len-1][s_len-1])