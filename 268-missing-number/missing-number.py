class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(nums[0] , nums[-1]):
            if nums[i]  != i:
                return i

        return nums[-1] + 1
        