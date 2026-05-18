class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n


    def find(self , x):

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self , a , b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if ra < rb:
            self.parent[ra] = rb

            self.rank[rb] += self.rank[ra]

        else:
            self.parent[rb] = ra

            self.rank[ra] += self.rank[rb]


        return True




class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        dsu = DSU(n)

        answer = []


        for edge in edges:
            a = edge[0]
            b = edge[1]

            temp = dsu.union(a-1 , b-1)
            if not temp :
                answer.append([a, b])

        return answer[-1]
