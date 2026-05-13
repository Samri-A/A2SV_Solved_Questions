from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)

        
        letter = ''
        max_freq = 0
        max_num = 0

        for key in freq:

            if freq[key] > max_freq:
                letter = key
                max_freq = freq[key]
            
        for key in freq:

            if freq[key] == max_freq:
                max_num += 1
            

        return  max(len(tasks) ,(max_freq - 1) * (n + 1) + max_num)

        