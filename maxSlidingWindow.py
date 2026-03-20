from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = deque()

        answer = []

        for i , num in enumerate(nums):
            
            while window and  nums[window[-1]] < num:
                window.pop()
            
            window.append(i)

            if i >= k - 1 :
                answer.append(nums[window[0]])
            
            if window[0] <= i - k + 1:
                    window.popleft()
                
            

        

        return answer
