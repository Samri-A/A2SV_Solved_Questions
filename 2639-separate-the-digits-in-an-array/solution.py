class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for i in nums:
            temp = str(i)
            if len(temp) > 1:
                for j in temp:
                    answer.append(int(j))
            else:
                answer.append(i)

        return answer
