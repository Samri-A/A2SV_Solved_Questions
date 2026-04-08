class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = None
        for i in range(1,len(nums)):  
            if nums[i] < nums[i-1]:
                pivot = i
                break

        if pivot is not None:
            return nums[i]
        else:
            return nums[0]
        
        