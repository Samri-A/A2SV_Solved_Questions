class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        result = None
        
        for i in range(n):
            left = i + 1
            right = n -1 

            while left < right:

                sumation = nums[i] + nums[left] + nums[right]

                if sumation == target:
                    return sumation
                
                if result is None:
                    result = sumation
                else:
                    if abs(target - result ) > abs(target - sumation):
                        result = sumation
                     




                if sumation < target:
                    left += 1
                else:
                    right -= 1

                

        # print(nums)



        return result