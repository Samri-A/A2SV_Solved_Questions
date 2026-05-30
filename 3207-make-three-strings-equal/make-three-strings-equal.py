class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i = 0
        prefix = 0

        while i < len(s1) and i < len(s2) and i < len(s3):
            if s1[i] == s2[i] == s3[i]:
                prefix += 1
                i += 1
            else:
                break
        
        if prefix > 0:
            d_s1 = len(s1) - prefix
            d_s2 = len(s2) - prefix
            d_s3 = len(s3) - prefix

            return d_s1 + d_s2 + d_s3
        else:
            return -1