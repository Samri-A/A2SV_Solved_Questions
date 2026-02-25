class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        chars_last_index = {}
        for i in range(len(s)):
            chars_last_index[s[i]] = i

        size = 0
        end = 0
        partition_sizes = []
        for i in range(len(s)):
            if chars_last_index[s[i]] > end:
                end = chars_last_index[s[i]]
            
            size+=1
            if i == end:
                partition_sizes.append(size)
                size = 0


        return   partition_sizes

