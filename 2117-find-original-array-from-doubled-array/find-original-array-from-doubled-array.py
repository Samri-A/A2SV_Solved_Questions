from collections import Counter
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        original  = []
        if len(changed)%2 != 0:
            return []
        

        
        num_counter = Counter(changed)

        changed.sort()

        for j in changed:
            if num_counter[j] == 0:
                continue
            
            if num_counter[j*2] == 0:
                return []
            
            num_counter[j] -= 1
            num_counter[j*2] -=1
            original.append(j)
       
        return original
        

        