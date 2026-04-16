from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        missing = 0
        duplicate = 0

        
        for i in range(1, len(nums)+1):
            if i in freq and freq[i] > 1:
                duplicate = i
            elif i not in freq:
                missing = i
                 
        

        return [duplicate ,  missing]

