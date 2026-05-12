from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        outgoing = [0] * n
        reversed_graph = defaultdict(list)

        for i in range(n):
            outgoing[i] = len(graph[i])
            for neb in graph[i]:
                reversed_graph[neb].append(i)
        
        

        queue = deque()
        for i in range(n):
            if outgoing[i] == 0:
                queue.append(i)


        result = []

        while queue:

            current = queue.popleft()
            result.append(current)

            for neb in reversed_graph[current]:

                outgoing[neb] -= 1

                if outgoing[neb] == 0:
                    queue.append(neb)

        
       
        return sorted(result)

     