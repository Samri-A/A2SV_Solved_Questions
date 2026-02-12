class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        t_hash = {
            
        }
        steps =  0
        for i in t:
            if i in t_hash:
                t_hash[i] +=1

            else:
                t_hash[i] = 1


        for j in s:
            if j in t_hash:
                t_hash[j] -=1
                if t_hash[j] == 0:
                    del t_hash[j]
            else:
                steps+=1
        

        return steps

        