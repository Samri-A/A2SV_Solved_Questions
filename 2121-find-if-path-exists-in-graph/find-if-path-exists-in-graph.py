class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

        def dfs(source, distination, graph, visited):
            ans = False
            if source == distination:
                ans = True
                return True

            for nei in graph[source]:
                if visited[nei] == False:
                    visited[nei] = True
                    if dfs(nei, distination, graph, visited):
                        return True

            return False

        visited = [False] * n
        return dfs(source, destination, graph, visited)