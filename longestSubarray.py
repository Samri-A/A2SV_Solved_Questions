from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minmum = deque()
        maximum = deque()

        left = 0
        right = 0

        sub_long = 0

        while right < len(nums):

            while maximum and  maximum[-1] < nums[right]:
                maximum.pop()

            maximum.append(nums[right])

            while  minmum and minmum[-1] > nums[right]:
                minmum.pop()

            minmum.append(nums[right])

            while  maximum[0] - minmum[0] > limit:
                

                if maximum[0] == nums[left]:
                    maximum.popleft()

                if minmum[0] == nums[left]:
                    minmum.popleft()
                left += 1
            
            sub_long = max( right - left + 1, sub_long)

            right += 1

        return sub_long

