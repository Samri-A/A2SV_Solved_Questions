class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        answer = [0] * len(indices)

        for i in range(len(s)):
            answer[indices[i]] = s[i]

        suf = ''
        for i in answer:
            suf += i
        return suf
        