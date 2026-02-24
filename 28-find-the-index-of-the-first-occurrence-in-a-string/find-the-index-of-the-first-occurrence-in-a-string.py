class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if needle_size is in the haystack
        if needle not in haystack:
            return -1

        
        needle_size = len(needle)
        
        # get the first indice of the needle_size
        for i in range(len(haystack)):
            if haystack[i:i+needle_size] == needle:
                return i
        


        
