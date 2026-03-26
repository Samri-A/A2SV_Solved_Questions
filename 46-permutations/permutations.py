class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        path = []

        arr =  []

        def backtrack():
            if len(nums) <= 0:
                return

            if len(path) == len(nums):
                arr.append(path.copy())
                return 

            
            for i in range(len(nums)):
                if nums[i] in path:
                    continue 
                path.append(nums[i])
                backtrack()
                path.pop()

            

        backtrack()
        return arr

            