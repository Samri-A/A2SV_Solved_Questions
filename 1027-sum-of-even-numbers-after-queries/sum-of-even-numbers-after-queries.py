class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_sum = 0
        for j in nums:
                if j%2 == 0:
                    even_sum+=j
        answer = []
        for i in queries:
            index = i[1]
            val = i[0]
            temp = nums[index]
            nums[index] = nums[index] + val
            if temp%2 == 0 : even_sum -= temp 
            if nums[index]%2 == 0 : even_sum += nums[index]
            answer.append(even_sum)

        
        return answer
        