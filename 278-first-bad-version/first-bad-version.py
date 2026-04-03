# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n 

        mid = (left + right) // 2

        first_bad = n
        while left <= right:
            print(mid)
            if isBadVersion(mid):
                first_bad = min(mid , first_bad)
                right = mid - 1
                    
            else:
                left = mid + 1
            mid = (left + right) // 2

            
        return first_bad 
        