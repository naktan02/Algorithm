import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))

def dfs(start):
    if not tree[start]:
        return (0,0)
    max_solo = 0
    max_group = 0
    for now, cost in tree[start]:
        a,b= dfs(now)
        cost+=a
        max_group = max(max_group,b,max_solo+cost)
        max_solo = max(max_solo, cost)
    return (max_solo, max_group)

a,b = dfs(1)
print(b)
        

