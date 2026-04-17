import heapq 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        for j in range(k):
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    temp = nums[i]
                    nums[i] = nums[i-1]
                    nums[i-1] = temp

        # print(nums)
        answer = nums[-(k)]
        return answer