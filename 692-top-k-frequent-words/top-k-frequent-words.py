from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)


        buckets = [ []  for i in range(len(words))  ]


        for key in freq:

            buckets[freq[key]].append(key)







        print(buckets)
        result = []
        for bucket in  reversed(buckets)  :
            bucket.sort()
            for word in bucket:
                result.append(word)
                if len(result) == k:
                    return result
            
            if len(result) == k:
                    return result
        

        return result
        