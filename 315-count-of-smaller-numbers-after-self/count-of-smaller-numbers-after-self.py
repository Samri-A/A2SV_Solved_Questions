class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        result = []

        sorted_nums = []

        for i in range(len(nums)-1 , -1 , -1):

            if not sorted_nums:
                sorted_nums.append(nums[i])
                result.append(0)

            else:

                left = 0
                right = len(sorted_nums) 

                while left < right:

                    mid = (left+right ) // 2

                    if sorted_nums[mid] >= nums[i]:
                        right  = mid 
                    else:
                        left = mid + 1

                
                sorted_nums.insert(left ,  nums[i])
                
                result.append(left)

        

        return result[::-1]
