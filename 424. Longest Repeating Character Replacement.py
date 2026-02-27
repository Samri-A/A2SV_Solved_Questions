from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        freq_count = {}
        longest_len = 0
        while right < len(s):
            

            if s[right] in freq_count:
                freq_count[s[right]] += 1
            else:
                freq_count[s[right]] = 1

            # Count letters that need to be replaced and if it is less than the allowed k we will shrink our window from left
            moreletter = max(freq_count , key = freq_count.get)
            maxfreq = freq_count [moreletter]
            lessfreq = (right - left + 1) - maxfreq
            
            
            if lessfreq <= k :
                longest_len = max ( right - left + 1, longest_len)
                
            else:
                freq_count[s[left]] -= 1
                left += 1
               
                lessfreq = (right - left + 1) - freq_count [max(freq_count)] 
                longest_len = max ( right - left + 1, longest_len)
                
            right+=1
            

        return longest_len
        
