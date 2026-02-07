class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for key in count:
            if count[key] == 1:
                return key