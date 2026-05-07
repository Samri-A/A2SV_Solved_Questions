from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        graph = [[] for _ in range(numCourses)]
        incoming = [0] * numCourses

        for course , pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        
        # print(incoming)
        # print(graph)

        result = []

        queue = deque()

        for i in range(len(incoming)):
            if incoming[i] == 0 :
                queue.append(i)

        while queue:
            course = queue.popleft()
            result.append(course)


            for neb in graph[course]:
                incoming[neb] -= 1
                if incoming[neb] == 0:
                    queue.append(neb)

        if len(result) != numCourses:
            return []


        return result

