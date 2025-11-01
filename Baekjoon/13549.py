import heapq
n,k = map(int,input().split())
q = []
visited = [False]*100005
heapq.heapify(q)
heapq.heappush(q,(0,n))
result = 0
while True:
    count, index = heapq.heappop(q)
    visited[index] = True
    if index == k:
        result = count
        break
    for i in (index+1,index-1):
        if 0 <= i < 100005 and visited[i] == False:
            heapq.heappush(q,(count+1,i))
    if 0 <= 2*index < 100005 and visited[2*index] == False:
        heapq.heappush(q,(count,index*2))
        
print(result)