from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
       
        # pointer = 0
        slow = 0

        fast = 0
        while True:

            slow = nums[slow]
            
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow =  nums[0]
        fast =  nums[fast]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


