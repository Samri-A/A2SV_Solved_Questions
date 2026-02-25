from math import sqrt 
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        possibe_b_squared = set()

        num =  int(sqrt(c) ) + 1

        for b in range(0, num):
            possibe_b_squared.add(b**2)

        for a in range(0 , num):
            b = c - a**2
            if b in possibe_b_squared:
                return True

        
        
        return False
        
