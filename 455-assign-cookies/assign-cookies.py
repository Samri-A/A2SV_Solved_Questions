class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()

        pointer_g = 0
        pointer_s = 0

        cookies = 0

        while pointer_g < len(g) and pointer_s < len(s):

            if g[pointer_g] <= s[pointer_s]:
                cookies += 1
                pointer_g += 1
            
            
            pointer_s += 1

        return cookies
