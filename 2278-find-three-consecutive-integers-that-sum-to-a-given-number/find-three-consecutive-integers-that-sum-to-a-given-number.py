class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        temp = num / 3
        if num % 3 == 0:
            return [temp -1, temp , temp + 1 ]
        else:
            return []