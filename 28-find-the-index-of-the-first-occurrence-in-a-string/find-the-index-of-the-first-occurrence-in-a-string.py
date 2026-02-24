class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        
        needle_size = len(needle)
        
        for i in range(len(haystack)):
            if haystack[i:i+needle_size] == needle:
                return i
        


        