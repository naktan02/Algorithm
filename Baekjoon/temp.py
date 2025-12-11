import sys

input = sys.stdin.readline
n = int(input())
data_max = 0
for _ in range(n):
    a,b,c = map(int,input().split())
    if a == b+c:
        data_max = max(data_max,a*(b+c)*2)
    else:
        data_max = max(data_max,a*(b+c))
print(data_max)