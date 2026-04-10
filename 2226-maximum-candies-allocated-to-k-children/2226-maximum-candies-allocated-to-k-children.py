class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def each_get_candies(candy):

            child = 0

            for c in candies:
                child += c//candy

            return child >= k

        
        if sum(candies) < k:
            return 0
        
        else:
            left = 1
            right = max(candies)
            ans = 0

            while left <= right:
                mid = (left+right)//2

                if each_get_candies(mid):
                    ans = mid 
                    left = mid + 1
                else:
                    right = mid - 1
                
            return ans

        

        