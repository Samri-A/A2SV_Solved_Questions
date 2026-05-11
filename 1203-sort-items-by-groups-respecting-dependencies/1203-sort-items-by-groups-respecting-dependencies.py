from collections import deque
class Solution:

    def top_sort(self , indegree , n ,graph):
        queue = deque()

        res = []

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:

            current = queue.popleft()
            res.append(current)


            for neb in graph[current]:
                indegree[neb] -= 1

                if indegree[neb] == 0:
                    queue.append(neb)
        

        return res if len(res) == n else []



    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n

        

        newgroup_id = m

        for i in range(n):
            if group[i] == -1:
                group[i] = newgroup_id
                newgroup_id += 1

        totalgroup =  newgroup_id

        group_graph = defaultdict(list)
        indegree_group  = [0] *  totalgroup


        for i in range(n):
            for val in beforeItems[i]:
                graph[val].append(i)
                indegree[i] += 1

                if group[i] != group[val]:
                    group_graph[group[val]].append(group[i])
                    indegree_group[group[i]] += 1
        

        group_sort = self.top_sort( indegree_group  , totalgroup  , group_graph )
        item_sort = self.top_sort( indegree , n, graph)

        if not group_sort or not item_sort:
            return []

        grouped_item = defaultdict(list)

        for item in item_sort:
            grouped_item[group[item]].append(item)

        result = []

        for group in group_sort:
            result.extend(grouped_item[group])

        return result 


        
