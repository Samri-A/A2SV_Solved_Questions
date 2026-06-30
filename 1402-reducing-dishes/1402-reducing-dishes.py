class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        max_time = 0 

        for i in range(n):
            time = 1
            cont = 0
            for j in range(i, n):
                cont += (time * satisfaction[j])
                time+=1
                
                max_time = max(max_time  , cont)

        return max_time