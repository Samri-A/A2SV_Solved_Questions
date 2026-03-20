class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        right = len(nums) - 2

        replacement = 0
        while right >= 0:

            if nums[right] > nums[right+1]:

                d = nums[right] // nums[right+1]       

                if  nums[right] % nums[right+1] != 0 : d +=1

                replacement += d - 1

                nums[right] = nums[right] // d

            right -=1

        return replacement

