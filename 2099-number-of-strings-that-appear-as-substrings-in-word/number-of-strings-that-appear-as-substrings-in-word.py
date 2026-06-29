class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        count = 0
        for pattern in patterns:
            temp = word.find(pattern)
            if temp != -1:
                count += 1
            # print(pattern , temp)
        
        return count