class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        prefix_sum = {0:-1}

        sum_ = 0
        for i  in range(len(nums)) :
            sum_ += nums[i]
            mod = sum_%k if k !=0 else sum_

            if sum_%k == 0 and i >= 1:
                return True

            if sum_%k in prefix_sum: 
                if i - prefix_sum[mod] >= 2: return True

            else: prefix_sum[mod] = i 

    

        return False
