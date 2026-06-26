class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[None] * n for i in range(m)]
        # print(dp)

        def dfs(x,y):
            if x == (m-1) and y==(n-1):
                if obstacleGrid[x][y]: return 0
                return 1

            if x >= m or y >= n:
                return 0

            if dp[x][y] is None:
                if obstacleGrid[x][y]:
                    dp[x][y] = 0 
                    return dp[x][y]
                else:
                    dp[x][y] = dfs(x+1, y) + dfs(x, y+1)
                    return dp[x][y]
            else:
                
                return dp[x][y]

        val = dfs(0,0)
        print(dp)
        return val