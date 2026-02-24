class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        max = 0 
        while left < right :
            temp = height[right] * ((right -1 ) - left)
            if height[right] > height[left]:
                temp = height[left] * (right  - left)
                left+=1
            else :
                temp = height[right] * (right - left)
                right -=1
            if temp > max :
                max = temp
        if len(height) == 2:
            return min(height)
        return max
        