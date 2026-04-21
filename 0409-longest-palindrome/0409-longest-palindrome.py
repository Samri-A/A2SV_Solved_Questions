from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)

        one_letter = 0

        len_letter = 0

        for key in freq:
            if freq[key]%2 == 0:
                len_letter += freq[key]
            else:
                if one_letter == 0:
                    one_letter += freq[key]
                else:
                    len_letter += freq[key] - 1
        print(freq)

        return one_letter + len_letter