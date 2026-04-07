class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_operations = 0

        window_size = 3

        left = 0
        right = 2

        while right < len(nums):

            if nums[left] == 0:
                for i in range(window_size):
                    if nums[left+i] == 0:
                        nums[left+i] = 1
                    else: nums[left+i] = 0
                count_operations+=1

            left+=1
            right+=1

        # print(nums)
    
        return count_operations if nums.count(0)== 0 else -1