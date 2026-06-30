from functools import cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7
        
        @cache
        def dsf(x,y,maxMove):
            if x >= m or y >= n or x < 0 or y < 0 :
                return 1

            if maxMove == 0:
                return 0
            
            res = (dsf(x-1 , y , maxMove-1) + dsf(x , y-1 , maxMove-1) + dsf(x+1 , y , maxMove-1) + dsf(x, y+1 , maxMove-1))
            
            return res%mod
           



        
        return dsf(startRow , startColumn ,maxMove )
        