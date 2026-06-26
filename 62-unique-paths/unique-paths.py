class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None] * n for _ in range(m)]
        
        def bfs(x, y):
            if x == (m-1) and y == (n-1):
                return 1
            
            if x >= m or y >= n:
                return 0

            if dp[x][y]:
                return dp[x][y]
            else:
                dp[x][y] = bfs(x, y+1) + bfs(x+1, y)
                return dp[x][y]

        val = bfs(0, 0)
        # print(dp)
        return val