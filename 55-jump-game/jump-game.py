class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_index = 0

        for i in range(len(nums)-1):

            if max_index < i:
                return False
                
            temp = i + nums[i]

            max_index = max(temp , max_index )


        
        print(max_index)
        
        return max_index >= len(nums)-1