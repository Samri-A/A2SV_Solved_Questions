from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # basecase : finish nums
        # how many  len(nums) ** 2 state
        # 
        n = len(nums)

        
        @cache
        def dsf(i , sum_):
            if i == n :
                return 1 if target == sum_ else 0

            
            res = dsf(i+1 , sum_ + nums[i]) + dsf(i +1, sum_ - nums[i])
            return res

        return dsf(0, 0)