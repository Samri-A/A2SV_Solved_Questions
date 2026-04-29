class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:

        nums.sort()

        median_sum = 0

        left = 0
        right = len(nums) -1 

        while left < right:

            median_sum += nums[right-1]

            right -= 2

            left += 1
        

        return median_sum

        