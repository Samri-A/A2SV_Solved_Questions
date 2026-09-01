from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = [[] for i in range(len(nums)+1)] 
        
        freq = Counter(nums)

        for key in freq:
            store[freq[key]].append(key)


        res = []

        for i in range(len(store)-1 , 0 , -1):

            for n in store[i]:
                res.append(n)
                
                if len(res) == k:
                    return res

        # print(store , freq)

        return res

