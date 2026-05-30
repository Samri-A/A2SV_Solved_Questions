from collections import Counter
class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:

        freq = Counter(nums)
        arr = []


        while freq:
            temp = []
            todel = []
            for key in freq:
                freq[key] -= 1
                temp.append(key)
                if freq[key] == 0:
                    todel.append( key)

            arr.append(temp)
            for item in todel:
                del freq[item]

        return arr
                



        
        