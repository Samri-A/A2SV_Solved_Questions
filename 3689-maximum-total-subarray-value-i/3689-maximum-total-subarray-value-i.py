class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
       
        
        
        max_ = max(nums)
        min_ = min(nums)

        
        return k * (max_) - k * (min_)
            

        