from collections import Counter
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:

        

        reminder = Counter( num%space for num in nums)

        
        max_ = max(reminder.values())
        ans = float('inf')

        for num in nums:
            if reminder[num%space] == max_:
                ans = min(ans , num)

        print(reminder)

        return ans if ans != float('inf') else min(nums)
        