from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)

        freq_heap = []
        heapq.heapify(freq_heap)


        for key in freq:
            heapq.heappush( freq_heap , (-freq[key], key))

        result = []
        for i in range(k):
            val , word =  heapq.heappop(freq_heap)
            result.append(word)

        return result

        