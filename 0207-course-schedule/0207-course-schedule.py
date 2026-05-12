from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses

        graph = defaultdict(list)

        for course , pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neb in graph[current]:

                indegree[neb] -= 1

                if indegree[neb] == 0:
                    queue.append(neb)

        
        return True if len(result) == numCourses else False