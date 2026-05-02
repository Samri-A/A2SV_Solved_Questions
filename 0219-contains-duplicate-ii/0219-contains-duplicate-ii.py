from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        k_range = {}

        

        left = 0
        k_left = 0


        while left < len(nums):

            if nums[left] in k_range:
                return True
            else:
                k_range[nums[left]] = 1  

            if left - k_left >= k:
                del k_range[nums[k_left]]
                k_left += 1

            left += 1

        
        return False