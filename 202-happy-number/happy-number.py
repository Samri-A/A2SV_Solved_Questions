class Solution(object):
    def __init__(self):
        self.seen_values = {}

    def Sum_the_squared(self , n):
        str_n = str(n)
        sumation = 0
        for i in str_n:
            sumation += int(i)**2

        if sumation == 1: return True 
        else: 
            if sumation in self.seen_values: return False 
            self.seen_values[sumation] = 1
            return self.Sum_the_squared(sumation)

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.Sum_the_squared(n)

        
