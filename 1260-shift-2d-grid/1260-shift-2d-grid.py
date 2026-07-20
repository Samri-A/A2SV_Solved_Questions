class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])


        for _ in range(k):
            ans = [[0] * col for _ in range(row)]
            for i in range(row):
                for j in range(col):
                    if col > (j + 1):
                        ans[i][j+1] = grid[i][j]
                    else:
                       tras_i =( i+1)%row
                       ans[tras_i][0] = grid[i][j]

            
            grid = ans

        

        return grid


