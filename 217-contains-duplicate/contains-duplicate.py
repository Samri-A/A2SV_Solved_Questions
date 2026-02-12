class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i-1] : 
                    return True

        return False 
        