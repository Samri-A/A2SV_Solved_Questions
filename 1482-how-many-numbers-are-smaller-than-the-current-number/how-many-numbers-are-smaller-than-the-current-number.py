class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count_lessnums = {
            sorted_nums[0]: 0
        }
        counter = 0
        num = sorted_nums[0]

        for i in range(len(sorted_nums)):
            
            if num != sorted_nums[i]:
                num = sorted_nums[i]
                counter = i
                count_lessnums[num] = counter
            else:
                count_lessnums[num] = counter


        
        smalls = []
        print(count_lessnums)
        for i in nums:
            smalls.append(count_lessnums[i])
        
        return smalls
        
