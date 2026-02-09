class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {} 
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] +=1

        result = []
        sorted_freq = sorted(freq.items() , key =lambda x :  x[1] , reverse=True)
        print(sorted_freq)
        i = 0
        for key , count in sorted_freq:
            print(count)
            if i < k:
                result.append(key)
            i+=1
        return result


