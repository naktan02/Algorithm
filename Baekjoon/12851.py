n,k = map(int,input().split())

from collections import deque
queue = deque()
queue.append((n,0))
least = float(10000000)
count =0
check = [0]*100001
while queue:
    x,cnt = queue.popleft()
    if cnt > least or x < 0 or x > 100000:
        continue
    if x == k:
        least = cnt
        count += 1
        continue
    for nx in (x*2,x+1,x-1):
        if nx < 0 or nx > 100000:
            continue
        if check[nx] == 0 or check[nx] >= cnt+1:
            check[nx] = cnt + 1
            queue.append((nx,cnt+1))

print(least)
print(count)
