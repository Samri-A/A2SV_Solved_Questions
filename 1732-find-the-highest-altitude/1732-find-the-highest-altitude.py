class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        pre_sum = 0
        ans = 0 

        for h in gain:
            pre_sum += h
            ans = max(ans , pre_sum)

        return ans