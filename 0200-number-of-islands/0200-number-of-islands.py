from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        
        is_land = 0

        visted = set()

        rows , cols = len(grid) , len(grid[0])

        q = deque()

        def bfs(row , col):
            q = deque()

            visted.add((row , col))
            q.append((row , col))

            while q:

                r , c = q.popleft()

                direction = [[-1 , 0] , [0 , -1] , [1, 0] ,[0 , 1] ]

                for dr in direction:

                    d_r = r + dr[0]
                    d_c = c + dr[1]

                    if d_r in range(rows) and d_c in range(cols) and (d_r , d_c) not in visted and grid[d_r][d_c] == "1":
                        q.append((d_r , d_c))
                        visted.add((d_r , d_c))





        for row in range(rows):
            for col in range(cols):
                if  grid[row][col] == "1" and  (row , col ) not in visted:
                    bfs(row , col)
                    is_land += 1


        return is_land
        