class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        # The left will keep track of the zeros if 

        ones_len = 0

        left = -1
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                longest = max(ones_len , longest)
                if left != -1 :
                    ones_len = len(nums[left:right])
                    # print(ones_len)
                else:
                    ones_len+=1
                left = right
            else:
                ones_len+=1
            right+=1

        longest = max(ones_len , longest) - 1
        return longest

        