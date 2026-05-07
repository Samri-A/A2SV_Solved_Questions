from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = [[] for _ in range(n)]

        for ans , child in edges:
            graph[child].append(ans)

        
        result = []

        for node in  range(n):
            ancestors = set()
            queue = deque()
            queue.append(node)

            while queue:
                current = queue.popleft()
                for parent in graph[current]:
                    if parent not in ancestors:
                        ancestors.add(parent)
                        queue.append(parent)

            result.append(sorted(ancestors))


        return result