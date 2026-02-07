class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ordered = []
        for i in strs:
            ordered.append("".join(sorted(i)))

        answer = []
        len_un = len(ordered)
        tracker = {}
        pointer = 0
        for i in range(len(ordered)):
            if ordered[i] in tracker: continue 
            temp = []
            temp.append(strs[i])
            for j in range( i + 1 , len(ordered)):
                if ordered[i]  == ordered[j]:
                    temp.append(strs[j])
            
            if len(temp) > 1:
                answer.append(temp)
                tracker[ordered[i]] = 1
            else:
                answer.append([strs[i]])
        return answer
                 

        print(ordered)