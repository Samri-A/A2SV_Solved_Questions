class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        last = 0
        res = [words[last]] 

        for i in range(1,len(words)):

            if groups[last] != groups[i]:
                last = i
                res.append(words[last])

        return res
