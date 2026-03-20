class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        freq = {}
        for answer in answers:
            if answer + 1 not in freq:
                freq[answer + 1] = answer 
                total +=  answer + 1
            elif freq[answer + 1] == 0 : 
                freq[answer + 1] = answer 
                total +=  answer + 1
            else: 
                freq[answer + 1] -=  1

        return total
