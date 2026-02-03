class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        for i in range(len(strs[0])):
            for str_ in strs[1:]:
                if i == len(str_) or str_[i] != strs[0][i]:
                    return result

            result += strs[0][i]

        return result
