class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        x1 = s1.count('x')
        x2 = s2.count('x')
        if (x1+x2 )%2 !=0:
            return -1
        
        y1 = s1.count('y')
        y2 = s2.count('y')
        
        
        swap = 0
        xy_miss = 0
        yx_miss = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            elif s1[i] == 'x' and s2[i] == 'y':
                xy_miss+=1
                
            elif s1[i] == 'y' and s2[i] == 'x':
                yx_miss+=1

        swap = (yx_miss/2) +(xy_miss/2)
        if xy_miss%2 !=0:
            swap+=2

        return swap
