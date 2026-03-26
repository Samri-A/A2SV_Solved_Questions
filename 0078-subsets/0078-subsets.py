class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        path = []

        def backtrack(i):

            if len(nums) <= i:
                subset.append(path.copy())
                return 

            path.append(nums[i])
            

            print(path)

            backtrack(i+1)

            path.pop()

            backtrack(i+1)





        backtrack(0)

        return subset
