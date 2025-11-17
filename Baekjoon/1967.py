import sys
input = sys.stdin.readline
n = input()
tree = [[] for _ in range(n + 1)]
for _ in range(n):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))

def dfs(start):
    if not tree[start]:
        return 0
    max_solo = 0
    max_group = 0
    for node,weight in tree[start]:
        plus = dfs(node)
        if max_solo < weight + plus:
            max_solo = weight + plus
        elif max_solo + plus + weight > max_group:
            max_group = max_solo + plus + weight
        
