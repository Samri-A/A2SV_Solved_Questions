from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
       n = len(candyType)
       freq = Counter(candyType)
       half = n/2
       
       for key in freq:
        freq[key] -= 1
        if half >= 1:
            half -= 1
        else:
            break
        
       return int((n/2) - half)
