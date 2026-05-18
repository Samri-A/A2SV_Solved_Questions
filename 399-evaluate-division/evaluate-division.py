class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        weight = {}
        parent = {}

        def add(x):
            if x not in parent:
                parent[x] = x 
                weight[x] = 1.0

        def find(x):
            if x != parent[x]:
                root, w= find(parent[x])
                parent[x]  = root
                weight[x] *= w
            return parent[x] , weight[x]

        def union(x, y , value):
            add(x)
            add(y)

            px , wx = find(x)
            py , wy = find(y)

            if px != py:
                parent[px] = py
                weight[px] = value * ( wy / wx) 

        for (x , y) , v in zip(equations , values):
            union(x , y , v)

        result = []
        for x , y in queries:
            

            if x not in parent or y not in parent:
                result.append(-1.0)
                continue

            px ,wx = find(x)
            py , wy = find(y)

            if px != py:
                result.append(-1.0)
            else:
                result.append(wx/wy)

        return result



        