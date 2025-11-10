import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n,m = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]

data = list(map(int,sys.stdin.readline().split()))
if len(data) > 1:
    trust = data[1:]
else:
    trust = [0]

parts = []
for _ in range(m):
    line = list(map(int,sys.stdin.readline().split()))
    temp = line[1:]
    parts.append(temp)

for part in parts:
    if len(part) <= 1:
        continue
    first = part[0]
    for person in part[1:]:
        union(first, person)

truth_roots = set()
for person in trust:
    truth_roots.add(find(person))

ans = 0
for part in parts:
    can_lie = True
    for person in part:
        if find(person) in truth_roots:
            can_lie = False
            break
    if can_lie:
        ans += 1

print(ans)