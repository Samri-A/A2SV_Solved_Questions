class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True


        graph = defaultdict(list)

        for v , u in edges:
            graph[v].append(u)
            graph[u].append(v) 

        seen = set()
        
        def dfs(current):

            if current == destination:
                return True

            for n_node in graph[current]:

                if n_node not in seen:
                    seen.add(n_node)
                    if dfs(n_node):
                        return True

            return False

        return dfs(source)



