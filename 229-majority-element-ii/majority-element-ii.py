class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) // 3
        count_tracker = {}
        for i in nums:
            if i in count_tracker:
                count_tracker[i] += 1
            else:
                count_tracker[i] = 1
            
        answer = []    
        for key in count_tracker:
            if count_tracker[key] > n:
                answer.append(key) 

        return answer

        