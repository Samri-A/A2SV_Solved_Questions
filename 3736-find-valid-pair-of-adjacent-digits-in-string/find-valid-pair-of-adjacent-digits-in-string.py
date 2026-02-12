class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_freq = {}
        for i in s:
           if i in  count_freq:
              count_freq[i] +=1
           else:
              count_freq[i] = 1
        pair = ""
        for j in range(len(s)):
            if s[j] in  count_freq:
                if count_freq[s[j]] == int(s[j]) and  j+1 < len(s):

                    if s[j+1] in  count_freq:
                        if count_freq[s[j+1]] == int(s[j+1]) and s[j] != s[j+1] :
                            pair += s[j]
                            pair += s[j+1]
                            return pair

            if len(pair) == 2: break
        
        if len(pair) != 2: return ""

        

        return pair