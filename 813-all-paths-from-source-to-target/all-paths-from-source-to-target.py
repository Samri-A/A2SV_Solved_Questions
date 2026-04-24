class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        graph_ = defaultdict(list)

        for i in range(len(graph)):
            for node in graph[i]:
                graph_[i].append(node)

        

        result = []

        path = [0]
        
        def dfs(i):

            if i == len(graph) - 1:
                result.append(path.copy())
                return

            
            for neb_node in graph_[i]:

                    path.append(neb_node)
                    dfs(neb_node)
                    path.pop()
            

        dfs(0)

        return result