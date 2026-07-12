from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)


        ans = 0
        edge = [0]
        visted = set()
        def dfs(i):

            if i in visted:
                return 

            
            visted.add(i)

            for neb in graph[i]:
                edge[0] +=1
                dfs(neb )
        for i in range(n):
            node = len(visted)
            edge[0] = 0
            dfs(i)
            node = len(visted) - node
            if node and edge[0]/2 == ( node * (node  - 1))/2:
                ans += 1   
        
        return ans


         