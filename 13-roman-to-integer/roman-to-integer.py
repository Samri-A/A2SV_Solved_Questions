class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        convertToValue = {                            
                'I' : 1,
                'V'  : 5,
                 'X'  : 10,
                 'L'  : 50, 
                'C' : 100,
                'D' : 500,
                 'M' :1000
        }

        sum = 0
        for i in range(len(s)):
            value = convertToValue[s[i]]
            if i+1 < len(s):
                if value <  convertToValue[s[i+1]]:
                    value = -value
            sum += value

    

        return sum
        