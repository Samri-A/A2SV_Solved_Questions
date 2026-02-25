class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 1 and citations[0] > 0:
            return 1

        h_index = 0

        citations.sort()

        for i in range(len(citations)):
            print(len(citations) - i ,citations[i] )
            if len(citations) - i <= citations[i]:
               h_index = len(citations) - i 
               return   h_index
            
        return   h_index

        