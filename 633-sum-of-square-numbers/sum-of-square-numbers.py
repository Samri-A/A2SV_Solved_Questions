from math import sqrt 
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        possibe_b_squared = set()

        num =  int(sqrt(c) ) + 1

        for b in range(0, num):
            possibe_b_squared.add(b**2)

        for a in range(0 , num):
            b = c - a**2
            if b in possibe_b_squared:
                return True
        # nums = []
        # for i in range(1, num+1):
           
        #     nums.append(i)

        
        # if len(nums) == 1:
        #     if nums[0] ** 2 + nums[0] ** 2== c or  nums[0] ** 2 == c:
        #         return True

                
        # left = 0
        # right = len(nums) - 1
        # mid = len(nums)//2
        # while left < right:
        #     temp = nums[left] ** 2 + nums[right] ** 2
        #     if temp == c or nums[left] ** 2 == c or nums[right] ** 2 == c or nums[mid] ** 2 == c:
        #         return True
        #     elif nums[left] ** 2 + nums[mid] ** 2 > c:
        #         left+=1
        #         right = mid
        #     else:
        #         left = mid
        #         right -= 1

        
        
        return False
        