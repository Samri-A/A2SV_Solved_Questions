class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        prefix_sum = 0
        
        for i in nums:
            prefix_sum+= i
            min_prefix_sum = min(prefix_sum , min_prefix_sum )
        
        if min_prefix_sum < 1:
            return -(min_prefix_sum) + 1

        else:
            return 0
