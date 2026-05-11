from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        

        graph = defaultdict(list)
        indegree = [0] * (n)

        for prev , next_c in relations:
            graph[prev].append(next_c)
            indegree[next_c - 1] += 1

        queue = deque()
        dist = [0] * n


        for i in range(n):
            if indegree[i] == 0:
                queue.append(i+1)
                dist[i] = time[i]
        
        
        

        

        while queue:
            current = queue.popleft()

            for neb in graph[current]:

                dist[neb - 1] = max(dist[current-1] + time[neb - 1] ,  dist[neb - 1] )

                indegree[neb - 1] -= 1
                
                if indegree[neb - 1] == 0:
                    queue.append(neb)

        return max(dist)