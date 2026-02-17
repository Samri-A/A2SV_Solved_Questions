class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_with_index = list(enumerate(nums))
        number_with_index.sort(key= lambda x : x[1] )

        left = 0
        right = len(nums) - 1
        while left < right:
            sum = number_with_index[left][1] + number_with_index[right][1]
            if  sum == target:
                return [number_with_index[left][0] , number_with_index[right][0]]
            elif sum < target:
                left+=1
            else:
                right -=1

        return []
            

