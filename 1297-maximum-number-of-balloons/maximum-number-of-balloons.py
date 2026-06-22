class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # balloon
        word = {
            "b" : 0 , 
            "a" : 0,
            "l": 0,
            "o" : 0,
            "n" : 0 
        }

        for letter in text:
            if letter in word:
                word[letter] += 1

        
        ans = 0

        if min(word.values()) <= word["l"]//2 and min(word.values()) <= word["o"]//2:
            return  min(word.values())
        else:
            return min(word["l"]//2 , word["o"]//2)

        