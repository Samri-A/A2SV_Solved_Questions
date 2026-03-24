class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        sum_ = 0

        maxmium = sum(nums)

        
        for num in nums:
            if sum_ < 0:
                sum_ = 0
            
            sum_ += num
            maxmium = max(sum_ , maxmium)

        
        
        return maxmium