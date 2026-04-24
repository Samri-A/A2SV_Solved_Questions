from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        freq = Counter(nums)

        j = 0

        for i in range(len(nums)):
            while freq[j] == 0:
                j += 1
            
            nums[i] = j
            freq[j] -=1

        
