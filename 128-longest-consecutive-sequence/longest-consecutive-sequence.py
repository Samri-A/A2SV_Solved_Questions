class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        expected_number = nums[0]
        consecatives = [1] * len(nums)
        consecative_pointer = 0
        for i in range(1 , len(nums)):
            if nums[i] == expected_number + 1:
                consecatives[consecative_pointer] += 1
                expected_number += 1
            elif nums[i] == expected_number:
                continue
            else:
                consecative_pointer += 1
                expected_number = nums[i]

            

        return max(consecatives)
            
