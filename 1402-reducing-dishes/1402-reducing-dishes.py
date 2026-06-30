class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        max_time = 0 
        sufix = 0
        score = 0
        for i in range(n-1 , -1, -1):
            sufix += satisfaction[i] 
            score += sufix
            max_time = max(max_time  , score)

        return max_time