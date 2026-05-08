from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0] * n
        
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        

        
        queue = deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        


        remaning_node = n


        while remaning_node > 2:
            leaf_count = len(queue)
            remaning_node -= leaf_count

            for _ in range(leaf_count):
                current = queue.popleft()
                
                for neb in graph[current]:
                    degree[neb] -= 1
                    if degree[neb] == 1:
                        queue.append(neb)
                    
                    


        return list(queue)

