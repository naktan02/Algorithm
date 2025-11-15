class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1]*n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x,y = y,x
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True

edges = [(0,1),(1,2),(3,4)]
uf = UnionFind(5)

uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print(uf.parent)
print(uf.size)
print(uf.find(0))