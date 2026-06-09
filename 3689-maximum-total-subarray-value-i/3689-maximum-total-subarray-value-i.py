class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
       
        ans = 0
        n = len(nums)
        max_ = max(nums)
        min_ = min(nums)

        for i in range(k):
            

            ans += (max_ - min_)

        return ans
            

        