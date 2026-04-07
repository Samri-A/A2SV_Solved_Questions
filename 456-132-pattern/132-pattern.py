class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []

        medium = float('-inf')

        for i in range(len(nums)-1 ,-1 , -1):

            if nums[i] < medium:
                return True

            if not stack:
                stack.append(nums[i])
            else :
                while stack and  stack[-1] < nums[i]:
                    
                    medium = stack.pop()
                    
                stack.append(nums[i])
                
                    
                    
           


            # print(stack)
        return False