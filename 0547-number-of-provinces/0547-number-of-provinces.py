class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n   # can also be size

    def find(self, x):
        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        if ra == rb:
            return False  # already connected → cycle or no-op

        # union by rank
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
            self.rank[rb] += self.rank[ra]
        else:
            self.parent[rb] = ra
            self.rank[ra] += self.rank[rb]

        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)


        for i in range(n):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    dsu.union(i , j)

        province  = set()

        for i in range(n):
            province.add(dsu.find(i))

        
        return len(province)