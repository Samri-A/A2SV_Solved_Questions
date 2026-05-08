from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        answer = []

        graph = defaultdict(list)

        for pre , course in prerequisites:
            graph[course].append(pre)


        isReachable = [[False]  * numCourses for _ in range(numCourses) ]

        def bfs(node):
            isReachable[node][node] = True
            queue = deque()
            queue.append(node)

            while queue:
                current = queue.popleft()

                for neb in graph[current]:
                    if not isReachable[node][neb]:
                        queue.append(neb)
                        isReachable[node][neb] = True
        

        for i in range(numCourses):
            bfs(i)

        answer = []

        for pre , course in queries:
            answer.append(isReachable[course][pre])



        # print(isReachable)

        return answer