import sys
sys.setrecursionlimit(10**7)
data = list(map(int,sys.stdin.read().split()))


def postorder(start,end):
    if start > end:
        return
    index = start + 1
    root = data[start]
    while index <= end and data[index] < root:
        index +=1
    
    postorder(start+1,index-1)
    postorder(index,end)
    print(root)

postorder(0,len(data)-1)