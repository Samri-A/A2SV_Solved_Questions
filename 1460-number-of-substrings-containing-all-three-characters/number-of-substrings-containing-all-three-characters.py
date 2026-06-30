class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ocu = {}

        left = 0
        right = 0
        ans = 0
        n = len(s)

        while right < n:
            if s[right] not in ocu:
                ocu[s[right]] = 1
            else:
                ocu[s[right]] += 1

            while len(ocu) == 3:
                ans += (n-right)
                ocu[s[left]] -= 1

                if ocu[s[left]] == 0:
                    del ocu[s[left]]
            


                left += 1
             
            right += 1
        
        return ans