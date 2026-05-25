class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        def helper(day,canbuy):
            if day == n:
                return 0
            
            if dp[day][canbuy] != -1:
                return dp[day][canbuy]

            buy = float("-inf")
            sell = float("-inf")
            

            if canbuy:
                buy = - prices[day] + helper(day+1 , False)
            else:
                sell = prices[day] - fee + + helper(day+1 , True)

            moveon = helper(day+1 , canbuy)


            dp[day][canbuy] = max(buy , sell  , moveon)
            return dp[day][canbuy]

            

        return helper(0,1)