# 벨만 포드

import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m,w = map(int,input().split())
    edges = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        edges.append((a,b,c))
        edges.append((b,a,c))
    for _ in range(w):
        a,b,c = map(int,input().split())
        edges.append((a,b,-c))
    
    distance = [0] * (n+1)
    distance[1] = 0
    result = False
    for _ in range(n+1):
        check = False
        for a,b,c in edges:
            if distance[b] > distance[a] + c:
                distance[b] = distance[a] + c
                check = True
                if _ == n:
                    result = True
        if not check:
            break
    print("YES" if result else "NO")

