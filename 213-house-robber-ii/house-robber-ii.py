class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]


        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        
        for i in range(2, n-1): 
                       
            dp[i] = max( dp[i-1] , dp[i -2] + nums[i])

        if n < 3:
            return max(nums[0], nums[1])

        dp1 = [0] * n
        dp1[1] = nums[1]
        dp1[2] = max( nums[2], nums[1])

        for i in range(3, n): 
                       
            dp1[i] = max( dp1[i-1] , dp1[i -2] + nums[i])
        

        # print(dp , dp1)




        

        return dp[-2] if dp1[-1] < dp[-2] else dp1[-1]