class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # basically if a + b > c it is valid triangle
        
        perimeter = 0

        nums.sort()
        n = len(nums)
        for i in range( n-1 , -1 , -1):
            if i - 2 >= 0:
                a = nums[i -2 ] 
                b = nums[i -1 ]
                c = nums[i]

                if c < a + b:
                    perimeter = max( a+b+c, perimeter)
            else:
                break 

        return perimeter
            
