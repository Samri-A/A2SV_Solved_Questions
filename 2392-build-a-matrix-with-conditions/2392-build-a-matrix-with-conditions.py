from collections import deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        graph_row = defaultdict(list)
        graph_col = defaultdict(list)
        incoming_r  = [0] * (k + 1)
        incoming_c  = [0] * (k  + 1)



        for left , right in rowConditions:
            graph_row[left].append(right)
            incoming_r[right] += 1

        for above , below in colConditions:
            graph_col[above].append(below)
            incoming_c[below] += 1

        

        sorted_row = []

        sorted_col = []

        queue_r = deque()

        for i in range(k):
            if incoming_r[i + 1] == 0:
                queue_r.append(i + 1)

        
        while queue_r:
            current = queue_r.popleft()
            sorted_row.append(current)

            for neb in graph_row[current]:
                incoming_r[neb] -= 1
                if incoming_r[neb] == 0:
                    queue_r.append(neb) 

        print(sorted_row)

        queue_c = deque()

        for i in range(k):
            if incoming_c[i + 1] == 0:
                queue_c.append(i + 1)

        
        while queue_c:
            current = queue_c.popleft()
            sorted_col.append(current)

            for neb in graph_col[current]:
                incoming_c[neb] -= 1
                if incoming_c[neb] == 0:
                    queue_c.append(neb) 

        print(sorted_col)

        if len(sorted_col) != k or len(sorted_row) != k:
            return []

        result = [[0] * k for _ in range(k)]

        for i in range(len(sorted_row)):
            for j in range(len(sorted_col)):
                if sorted_col[j] == sorted_row[i]:
                    result[i][j] = sorted_col[j]
                    continue

        return result
        