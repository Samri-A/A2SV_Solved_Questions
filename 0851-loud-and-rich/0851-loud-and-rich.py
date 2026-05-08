from collections import deque
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = [[] for _ in range(len(quiet))]

        for rich , poor in richer:
            graph[poor].append(rich)

        print(graph)

        result = [-1] * len(quiet)

        def dfs(node):
            if result[node] != -1:
                    return result[node]
                    
            quietest = node

            for rich in graph[node]:

                current = dfs(rich)

                if quiet[current] < quiet[quietest]:
                    quietest = current
            

            result[node] = quietest
            return quietest

        for i in range(len(quiet)):
            q = dfs(i)

        return result






