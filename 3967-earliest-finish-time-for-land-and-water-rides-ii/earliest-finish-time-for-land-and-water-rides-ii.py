class Solution:
    def helper( self , la , ld , wa , wd):

        mine = float('inf')
        for i in range(len(la)):
            mine = min(mine , la[i] + ld[i])
        
        ans = float('inf')
        for i in range(len(wa)):
            ans = min(ans ,max( mine , wa[i])+wd[i])

        return ans




    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        return min(self.helper(landStartTime ,landDuration , waterStartTime , waterDuration) , self.helper(waterStartTime ,waterDuration, landStartTime , landDuration) )
        